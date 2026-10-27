#!/usr/bin/env python3
"""Sestaví veřejný web do ../site z domu.md, lekce/*.md, sablona.html a static/.

Lekce je jeden Markdown soubor: hlavička mezi --- a pod ní oddíly ## Nadpis {druh #id}.
Druhy oddílů: galerie, princip, potreby, postup, opravy, pribeh; bez druhu je obyčejný oddíl.
V textu: > tip nebo poznámka, ![popisek](fotka.jpg), {{nakres jmeno}}, {{model ...}}, {{stahnout ...}}.
"""
import hashlib
import re
import shutil
import struct
from pathlib import Path

from nakresy import NAKRESY

ZDROJ = Path(__file__).parent
VYSTUP = ZDROJ.parent / 'site'
PORADI = ['První', 'Druhá', 'Třetí', 'Čtvrtá', 'Pátá', 'Šestá', 'Sedmá', 'Osmá', 'Devátá', 'Desátá']
POPISKY = dict(
    (k.strip(), v.strip()) for k, v in
    (r.split('|', 1) for r in (ZDROJ / 'fotky.txt').read_text().splitlines() if r.strip() and not r.startswith('#'))
)


# --- čtení Markdownu ---

def nacti(soubor):
    _, hlavicka, telo = soubor.read_text().split('---\n', 2)
    meta = dict(r.split(': ', 1) for r in hlavicka.strip().splitlines())
    return meta, telo


def oddily(telo):
    """Vrátí úvodní text a seznam oddílů (nadpis, druh, id, text)."""
    casti = re.split(r'^## ', telo, flags=re.M)
    vysledek = []
    for cast in casti[1:]:
        radek, _, text = cast.partition('\n')
        m = re.fullmatch(r'(.+?)(?: \{(.+)\})?', radek.strip())
        znacky = (m[2] or '').split()
        druh = next((z for z in znacky if not z.startswith('#')), '')
        id_ = next((z[1:] for z in znacky if z.startswith('#')), '')
        vysledek.append((m[1], druh, id_, text))
    return casti[0], vysledek


def bloky(text):
    return [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]


def inline(t):
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', t)


# --- fotky a soubory ---

def rozmery(cesta):
    d = cesta.read_bytes()
    i = 2
    while i < len(d):
        znacka, delka = d[i + 1], struct.unpack('>H', d[i + 2:i + 4])[0]
        if 0xC0 <= znacka <= 0xCF and znacka not in (0xC4, 0xC8, 0xCC):
            vyska, sirka = struct.unpack('>HH', d[i + 5:i + 9])
            return sirka, vyska
        i += 2 + delka
    raise ValueError(f'{cesta}: nenašel jsem rozměry')


def img(soubor, lazy=True):
    if soubor not in POPISKY:
        raise SystemExit(f'Fotka {soubor} nemá popisek ve fotky.txt')
    w, h = rozmery(ZDROJ / 'static/foto' / soubor)
    return (f'<img src="/foto/{soubor}" alt="{POPISKY[soubor]}" width="{w}" height="{h}"'
            + (' loading="lazy">' if lazy else '>'))


def velikost(soubor):
    mb = (ZDROJ / 'static/modely' / soubor).stat().st_size / 1e6
    return f'{mb:.1f}'.replace('.', ',').removesuffix(',0') + ' MB' if mb >= 0.1 else ''


# --- vykreslení bloků ---

IKONA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 19h14"/></svg>'


def model(nahled, nazev, popis, soubor):
    return (f'<li>{img(nahled)}<h3>{nazev}</h3><p>{popis}</p>'
            f'<a href="/modely/{soubor}" download>Stáhnout {soubor.rsplit(".", 1)[1].upper()} ({velikost(soubor)})</a></li>')


def stahnout(soubor, nazev, popis, hlavni):
    if velikost(soubor):
        popis += f', {soubor.rsplit(".", 1)[1].upper()} {velikost(soubor)}'
    return (f'<a class="dl{"" if hlavni else " dl-alt"}" href="/modely/{soubor}" download>{IKONA}'
            f'<span><strong>{nazev}</strong><small>{popis}</small></span></a>')


def prikazy(blok):
    """Řádky {{...}} v jednom bloku; po sobě jdoucí modely a stahování se seskupí."""
    radky = [re.fullmatch(r'\{\{(\w+) ?(.*)\}\}', r.strip()).groups() for r in blok.splitlines()]
    druh = radky[0][0]
    argumenty = [[a.strip() for a in arg.split('|')] for _, arg in radky]
    if druh == 'nakres':
        return ''.join(NAKRESY[a[0]] for a in argumenty)
    if druh == 'model':
        return '<ul class="prints">' + ''.join(model(*a) for a in argumenty) + '</ul>'
    if druh == 'stahnout':
        return '<div class="downloads">' + ''.join(stahnout(*a, i == 0) for i, a in enumerate(argumenty)) + '</div>'
    raise SystemExit(f'Neznámý příkaz {{{{{druh}}}}}')


def trida(nazev):
    return f' class="{nazev}"' if nazev else ''


def md(text, ul='', p='', citace='tip'):
    vysledek = []
    for b in bloky(text):
        if b.startswith('{{'):
            vysledek.append(prikazy(b))
        elif b.startswith('- '):
            polozky = ''.join(f'<li>{inline(r[2:])}</li>' for r in b.splitlines())
            vysledek.append(f'<ul{trida(ul)}>{polozky}</ul>')
        elif b.startswith('> '):
            vysledek.append(f'<p class="{citace}">{inline(b[2:])}</p>')
        elif m := re.fullmatch(r'!\[(.*)\]\((.+)\)', b):
            vysledek.append(f'<figure>{img(m[2])}<figcaption>{m[1]}</figcaption></figure>' if m[1] else img(m[2]))
        elif b.startswith('<'):
            vysledek.append(b)
        else:
            vysledek.append(f'<p{trida(p)}>{inline(b)}</p>')
    return '\n'.join(vysledek)


# --- oddíly návodu ---

def galerie(text):
    figury = ''
    for r in text.strip().splitlines():
        soubor, popisek = r[2:].split(': ', 1)
        figury += (f'<figure><a href="/foto/{soubor}">{img(soubor, lazy=False)}</a>'
                   f'<figcaption>{popisek}</figcaption></figure>\n')
    return f'<div class="wrap">\n<div class="gallery">\n{figury}</div>\n</div>'


def oddil(nadpis, druh, id_, text, konec=''):
    if druh == 'princip':
        return f'<section class="principle">\n<h2>{nadpis}</h2>\n<div>\n{md(text)}\n</div>\n</section>'
    if druh == 'opravy':
        polozky = ''.join(
            '<div><dt>{}</dt><dd>{}</dd></div>\n'.format(*re.fullmatch(r'- \*\*(.+?)\*\* (.+)', r).groups())
            for r in text.strip().splitlines())
        obsah = f'<dl class="fixes">\n{polozky}</dl>'
    elif druh == 'pribeh':
        bb = bloky(text)
        fotky = [b for b in bb if b.startswith('![')]
        texty = [f'<p class="big-number">{b[2:-2]}</p>' if re.fullmatch(r'\*\*[^*]+\*\*', b) else md(b)
                 for b in bb if not b.startswith('![')]
        obsah = '<div class="story">\n<div>\n' + '\n'.join(texty) + '\n</div>\n' + md('\n\n'.join(fotky)) + '\n</div>'
    else:
        obsah = md(text, ul='more', p='section-lead')
    id_ = f' id="{id_}"' if id_ else ''
    return f'<section class="after"{id_}>\n<h2>{nadpis}</h2>\n{obsah}\n{konec}</section>'


def postup(potreby, kroky):
    polozky = ''
    for krok in re.split(r'^### ', kroky, flags=re.M)[1:]:
        nadpis, _, text = krok.partition('\n')
        polozky += f'<li>\n<div>\n<h3>{nadpis.strip()}</h3>\n{md(text)}\n</div>\n</li>\n'
    return (f'<div class="howto">\n<aside class="materials">\n<h2>{potreby[0]}</h2>\n'
            f'{md(potreby[1], citace="note")}\n</aside>\n'
            f'<div>\n<h2>Postup</h2>\n<ol class="steps">\n{polozky}</ol>\n</div>\n</div>')


def cislo(lekce):
    return (f'<p class="lesson-no"><span class="blob" style="--c: var(--{lekce["barva"]})">'
            f'<span>{lekce["cislo"]}</span></span>{PORADI[lekce["cislo"] - 1]} lekce</p>')


def maly(nazev):
    return nazev[0].lower() + nazev[1:]


def stranka_lekce(lekce, predchozi, dalsi):
    _, casti = oddily(lekce['telo'])
    obsah = [f'''<div class="guide-head">
<div class="wrap">
{cislo(lekce)}
<h1>{lekce["nazev"]}</h1>
<p class="lead">{lekce["perex"]}</p>
<ul class="meta">
<li><strong>Kdy:</strong> {lekce["kdy"]}</li>
<li><strong>Jak dlouho:</strong> {lekce["jak_dlouho"]}</li>
<li><strong>Domů:</strong> {lekce["domu"]}</li>
</ul>
</div>
</div>''']
    navigace = '<nav class="next" aria-label="Další lekce">\n'
    if predchozi:
        navigace += f'<a href="/{predchozi["adresa"]}/">Předchozí lekce: {maly(predchozi["nazev"])}</a>\n'
    navigace += '<a href="/">Zpět na přehled</a>\n'
    if dalsi:
        navigace += f'<a href="/{dalsi["adresa"]}/">Další lekce: {maly(dalsi["nazev"])}</a>\n'
    navigace += '</nav>\n'

    telo = []
    potreby = None
    for i, (nadpis, druh, id_, text) in enumerate(casti):
        if druh == 'galerie':
            obsah.append(galerie(text))
        elif druh == 'potreby':
            potreby = (nadpis, text)
        elif druh == 'postup':
            telo.append(postup(potreby, text))
        else:
            telo.append(oddil(nadpis, druh, id_, text, navigace if i == len(casti) - 1 else ''))
    obsah.append('<div class="wrap">\n' + '\n'.join(telo) + '\n</div>')
    return stranka(
        titulek=f'{lekce["nazev"]} – Bastlířská dílna',
        popis=f'{lekce["popis"]} Lekce technického kroužku Bastlířská dílna.',
        og_titulek=lekce['nazev'], og_popis=lekce['popis'], og_fotka=lekce['prehled_fotky'].split()[0],
        obsah='\n'.join(obsah))


# --- domovská stránka ---

def karta(lekce):
    fotky = '\n'.join(img(f) for f in lekce['prehled_fotky'].split())
    return f'''<article class="lesson">
<div class="lesson-photos">
{fotky}
</div>
<div>
{cislo(lekce)}
<h3>{lekce["nazev"]}</h3>
<p>{lekce["prehled"]}</p>
<p class="when">{lekce["prehled_kdy"]}</p>
<a class="button" href="/{lekce["adresa"]}/">{lekce["tlacitko"]}</a>
</div>
</article>'''


def stranka_domu(lekce):
    meta, telo = nacti(ZDROJ / 'domu.md')
    uvod, casti = oddily(telo)
    obsah = [f'''<section class="hero">
<div class="wrap">
<div>
<h1><span>Bastlířská</span><span>dílna</span></h1>
<p class="lead">{meta["perex"]}</p>
{md(uvod, p="facts")}
</div>
{(ZDROJ / "vez.svg").read_text()}
</div>
</section>''']
    for nadpis, druh, id_, text in casti:
        uvodni, _, plany = text.partition('\n### ')
        if druh == 'lekce':
            vnitrek = md(uvodni, p='intro') + '\n' + '\n'.join(karta(l) for l in lekce)
            trida = 'section done'
        else:
            polozky = ''
            for n, plan in enumerate(re.split(r'^### ', '### ' + plany, flags=re.M)[1:], start=len(lekce) + 1):
                nazev, _, popis = plan.partition('\n')
                polozky += (f'<li>\n<span class="blob"><span>{n}</span></span>\n'
                            f'<div>\n<h3>{nazev.strip()}</h3>\n{md(popis)}\n</div>\n</li>\n')
            vnitrek = md(uvodni, p='intro') + f'\n<ol class="plans">\n{polozky}</ol>'
            trida = 'section'
        obsah.append(f'<section class="{trida}" id="{id_}">\n<div class="wrap">\n<h2>{nadpis}</h2>\n{vnitrek}\n</div>\n</section>')
    return stranka(titulek='Bastlířská dílna', popis=meta['popis'], og_titulek='Bastlířská dílna',
                   og_popis=meta['og_popis'], og_fotka=meta['og_fotka'], obsah='\n\n'.join(obsah))


# --- šablona a zápis ---

def stranka(**hodnoty):
    html = (ZDROJ / 'sablona.html').read_text()
    for klic, hodnota in hodnoty.items():
        html = html.replace('{' + klic + '}', hodnota)
    # k odkazům na vlastní soubory přidá otisk obsahu, aby prohlížeč po změně nenačetl starou verzi z mezipaměti
    def otisk(m):
        cesta = VYSTUP / m[2].lstrip('/')
        if not cesta.is_file():
            return m[0]
        return f'{m[1]}="{m[2]}?v={hashlib.md5(cesta.read_bytes()).hexdigest()[:8]}"'
    return re.sub(r'(src|href)="(/[^"#?]*)"', otisk, html)


def main():
    lekce = []
    for soubor in sorted((ZDROJ / 'lekce').glob('*.md')):
        meta, telo = nacti(soubor)
        lekce.append(meta | {'telo': telo, 'cislo': int(soubor.name.split('-')[0])})

    shutil.rmtree(VYSTUP, ignore_errors=True)
    shutil.copytree(ZDROJ / 'static', VYSTUP, ignore=shutil.ignore_patterns('.DS_Store'))
    (VYSTUP / 'index.html').write_text(stranka_domu(lekce))
    for i, l in enumerate(lekce):
        predchozi = lekce[i - 1] if i > 0 else None
        dalsi = lekce[i + 1] if i + 1 < len(lekce) else None
        (VYSTUP / l['adresa']).mkdir()
        (VYSTUP / l['adresa'] / 'index.html').write_text(stranka_lekce(l, predchozi, dalsi))
    print(f'Hotovo: {VYSTUP} ({len(lekce)} lekcí)')


if __name__ == '__main__':
    main()
