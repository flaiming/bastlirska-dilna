#!/usr/bin/env python3
"""Sestaví veřejný web do ../site z domu.md, lekce/*.md, sablona.html a static/.

Lekce je jeden Markdown soubor: hlavička mezi --- a pod ní oddíly ## Nadpis {druh #id}.
Druhy oddílů: galerie, princip, bezpecnost, potreby, postup, opravy, pribeh; bez druhu je obyčejný oddíl.
Postupů může být víc, každý si vezme potřeby z oddílu těsně před sebou.
V textu: ### podnadpis, > tip nebo poznámka, ![popisek](fotka.jpg), {{nakres jmeno}}, {{model ...}}, {{stahnout ...}}.

Lekce bez fotek má místo `prehled_fotky` v hlavičce `prehled_nakres: jmeno`, karta pak ukáže nákres.

Rozpracovaná lekce má v hlavičce `zverejnit: 2026-11-03`. Do toho dne se na web nedostane,
v náhledu (build.py --koncepty, tedy make nahled) je vidět s označením „Koncept“.
"""
import contextlib
import datetime
import functools
import hashlib
import http.server
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

from nakresy import NAKRESY, vez

ZDROJ = Path(__file__).parent
VYSTUP = ZDROJ.parent / 'site'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
WEB = 'https://bastleni.oram.cz'
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
        elif b.startswith('### '):
            vysledek.append(f'<h3>{inline(b[4:])}</h3>')
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
        soubor, _, popisek = r[2:].partition(': ')
        figury += (f'<figure><a href="/foto/{soubor}">{img(soubor, lazy=False)}</a>'
                   + (f'<figcaption>{popisek}</figcaption>' if popisek else '') + '</figure>\n')
    return f'<div class="wrap">\n<div class="gallery">\n{figury}</div>\n</div>'


def oddil(nadpis, druh, id_, text, konec=''):
    if druh == 'princip':
        return f'<section class="principle">\n<h2>{nadpis}</h2>\n<div>\n{md(text)}\n</div>\n</section>'
    if druh == 'bezpecnost':
        # pravidla jako očíslovaný seznam „- **Pravidlo** vysvětlení“, ostatní bloky jako obvykle
        casti = []
        for b in bloky(text):
            if b.startswith('- **'):
                # číslují se jen pravidla, další seznam (co dělat, když se něco stane) už ne
                znacka = 'ul' if any('class="rules"' in c for c in casti) else 'ol'
                polozky = ''.join(
                    '<li><strong>{}</strong> {}</li>'.format(*(inline(x) for x in re.fullmatch(r'- \*\*(.+?)\*\* (.+)', r).groups()))
                    for r in b.splitlines())
                casti.append(f'<{znacka} class="rules">{polozky}</{znacka}>')
            else:
                casti.append(md(b, ul='more', citace='alarm'))
        id_ = f' id="{id_}"' if id_ else ''
        return f'<section class="safety"{id_}>\n<h2>{nadpis}</h2>\n' + '\n'.join(casti) + f'\n{konec}</section>'
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


def postup(nadpis, id_, potreby, kroky, barva):
    uvod, *kroky = re.split(r'^### ', kroky, flags=re.M)
    polozky = ''
    for krok in kroky:
        nazev, _, text = krok.partition('\n')
        polozky += f'<li>\n<div>\n<h3>{nazev.strip()}</h3>\n{md(text)}\n</div>\n</li>\n'
    id_ = f' id="{id_}"' if id_ else ''
    return (f'<div class="howto"{id_}>\n<aside class="materials">\n<h2>{potreby[0]}</h2>\n'
            f'{md(potreby[1], citace="note")}\n</aside>\n'
            f'<div>\n<h2>{nadpis}</h2>\n{md(uvod, p="section-lead")}\n<ol class="steps" style="--c: var(--{barva})">\n{polozky}</ol>\n</div>\n</div>')


def cislo(lekce):
    return (f'<p class="lesson-no"><span class="blob" style="--c: var(--{lekce["barva"]})">'
            f'<span>{lekce["cislo"]}</span></span>{PORADI[lekce["cislo"] - 1]} lekce</p>')


SIPKA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13m0 0-5.5-5.5M18 12l-5.5 5.5"/></svg>'


def sipka(lekce, popisek, trida):
    """Odkaz na sousední lekci se šipkou v barvě té lekce; bez lekce prázdné místo, aby mřížka seděla."""
    if not lekce:
        return '<span></span>'
    return (f'<a class="{trida}" href="/{lekce["adresa"]}/" style="--c: var(--{lekce["barva"]})">{SIPKA}'
            f'<span><small>{popisek}</small><strong>{lekce["nazev"]}</strong></span></a>')


def stranky(n):
    return f'{n} strana' if n == 1 else f'{n} strany' if n < 5 else f'{n} stran'


def nazev_pdf(lekce):
    return f'bastlirska-dilna-{lekce["adresa"]}.pdf'


def tlacitko_pdf(lekce, pocet_stran):
    if not pocet_stran:
        return ''
    return (f'<a class="dl dl-alt" href="/{lekce["adresa"]}/{nazev_pdf(lekce)}" download>{IKONA}'
            f'<span><strong>Stáhnout návod v PDF</strong><small>na tisk, A4, {stranky(pocet_stran)}</small></span></a>')


def koncept(lekce):
    """Štítek u lekce, která ještě není zveřejněná (jen v náhledu)."""
    if not lekce.get('koncept'):
        return ''
    d = lekce['zverejnit']
    return f'<p class="koncept">Koncept, na webu se objeví {d.day}. {d.month}. {d.year}</p>'


def stranka_lekce(lekce, predchozi, dalsi, pocet_stran=None):
    _, casti = oddily(lekce['telo'])
    obsah = [f'''<div class="guide-head">
<div class="wrap">
{koncept(lekce)}
{cislo(lekce)}
<h1>{lekce["nazev"]}</h1>
<p class="lead">{lekce["perex"]}</p>
<ul class="meta">
<li><strong>Kdy:</strong> {lekce["kdy"]}</li>
<li><strong>Jak dlouho:</strong> {lekce["jak_dlouho"]}</li>
<li><strong>Domů:</strong> {lekce["domu"]}</li>
</ul>
<p class="jen-tisk">Celý návod s fotkami: bastleni.oram.cz/{lekce["adresa"]}/</p>
{tlacitko_pdf(lekce, pocet_stran)}
</div>
</div>''']
    navigace = (f'<nav class="next" aria-label="Další lekce">\n{sipka(predchozi, "Předchozí lekce", "prev")}\n'
                f'<a class="home" href="/">Zpět na přehled</a>\n{sipka(dalsi, "Další lekce", "nxt")}\n</nav>\n')

    telo = []
    potreby = None
    for i, (nadpis, druh, id_, text) in enumerate(casti):
        if druh == 'galerie':
            obsah.append(galerie(text))
        elif druh == 'potreby':
            potreby = (nadpis, text)
        elif druh == 'postup':
            telo.append(postup(nadpis, id_, potreby, text, lekce['barva']))
        else:
            telo.append(oddil(nadpis, druh, id_, text, navigace if i == len(casti) - 1 else ''))
    obsah.append('<div class="wrap">\n' + '\n'.join(telo) + '\n</div>')
    return stranka(
        titulek=f'{lekce["nazev"]} – Bastlířská dílna',
        popis=f'{lekce["popis"]} Lekce technického kroužku Bastlířská dílna.',
        og_titulek=lekce['nazev'], og_popis=lekce['popis'], og_typ='article', adresa=f'/{lekce["adresa"]}/',
        og_obrazek=obrazek_sdileni(lekce['adresa']), og_alt=f'{lekce["nazev"]}, lekce kroužku Bastlířská dílna',
        obsah='\n'.join(obsah))


# --- domovská stránka ---

def karta(lekce):
    if 'prehled_fotky' in lekce:
        fotky, trida = '\n'.join(img(f) for f in lekce['prehled_fotky'].split()), 'lesson-photos'
    else:
        fotky, trida = NAKRESY[lekce['prehled_nakres']], 'lesson-photos lesson-drawing'
    return f'''<article class="lesson">
<div class="{trida}">
{fotky}
</div>
<div>
{koncept(lekce)}
{cislo(lekce)}
<h3>{lekce["nazev"]}</h3>
<p>{lekce["prehled"]}</p>
<p class="when">{lekce["prehled_kdy"]}</p>
<a class="button" href="/{lekce["adresa"]}/">{lekce["tlacitko"]}</a>
</div>
</article>'''


MESICE = ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'červenec', 'srpen', 'září', 'říjen', 'listopad', 'prosinec']


def kalendar():
    """Úterky od–do s vystřídanými skupinami a výjimkami z kalendar.txt, po měsících."""
    nastaveni, vyjimky = {}, {}
    for r in (ZDROJ / 'kalendar.txt').read_text().splitlines():
        if not r.strip() or r.startswith('#'):
            continue
        if '|' in r:
            datum, stav, poznamka = (x.strip() for x in r.split('|'))
            vyjimky[datetime.date.fromisoformat(datum)] = (stav, poznamka)
        else:
            k, v = r.split(':', 1)
            nastaveni[k.strip()] = v.strip()
    den, konec = datetime.date.fromisoformat(nastaveni['od']), datetime.date.fromisoformat(nastaveni['do'])
    prvni_rok = den.year
    mesice = {}
    while den <= konec:
        skupina = nastaveni['lichý týden' if den.isocalendar().week % 2 else 'sudý týden']
        stav, poznamka = vyjimky.get(den, ('', ''))
        trida = {'zrušeno': ' zruseno', 'nejisté': ' nejiste'}.get(stav, '')
        popis = poznamka if stav == 'zrušeno' else f'skupina {skupina}' + (f', {poznamka}' if poznamka else '')
        mesice.setdefault((den.year, den.month), []).append(
            f'<li class="termin skupina-{skupina.lower()}{trida}" data-datum="{den}">'
            f'<span class="den">{den.day}. {den.month}.</span><span class="kdo">{popis}</span></li>')
        den += datetime.timedelta(days=7)
    return '<div class="kalendar">\n' + '\n'.join(
        f'<div class="mesic"><h3>{MESICE[m - 1]}{"" if r == prvni_rok else f" {r}"}</h3>'
        f'<ol>{"".join(dny)}</ol></div>' for (r, m), dny in mesice.items()) + '\n</div>'


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
{vez()}
</div>
</section>''']
    for nadpis, druh, id_, text in casti:
        uvodni, _, plany = text.partition('\n### ')
        if druh == 'lekce':
            vnitrek = md(uvodni, p='intro') + '\n' + '\n'.join(karta(l) for l in lekce)
            trida = 'section done'
        elif druh == 'kalendar':
            vnitrek = md(uvodni, p='intro') + '\n' + kalendar()
            trida = 'section'
        else:
            # plán, ze kterého už je zveřejněná lekce, se vynechá sám
            hotove = {l['nazev'].lower() for l in lekce}
            plany = [p.partition('\n') for p in re.split(r'^### ', '### ' + plany, flags=re.M)[1:]]
            plany = [(nazev, popis) for nazev, _, popis in plany if nazev.strip().lower() not in hotove]
            polozky = ''
            for n, (nazev, popis) in enumerate(plany, start=len(lekce) + 1):
                polozky += (f'<li>\n<span class="blob"><span>{n}</span></span>\n'
                            f'<div>\n<h3>{nazev.strip()}</h3>\n{md(popis)}\n</div>\n</li>\n')
            vnitrek = md(uvodni, p='intro') + f'\n<ol class="plans">\n{polozky}</ol>'
            trida = 'section'
        obsah.append(f'<section class="{trida}" id="{id_}">\n<div class="wrap">\n<h2>{nadpis}</h2>\n{vnitrek}\n</div>\n</section>')
    return stranka(titulek='Bastlířská dílna', popis=meta['popis'], og_titulek='Bastlířská dílna',
                   og_popis=meta['og_popis'], og_typ='website', adresa='/', og_obrazek=obrazek_sdileni('domu'),
                   og_alt='Bastlířská dílna, technický kroužek pro děti', obsah='\n\n'.join(obsah))


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


class TichyServer(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@contextlib.contextmanager
def chrome():
    """Pustí site/ na náhodném portu a vrátí funkci, která otevře zadanou cestu v Chromu bez okna."""
    if not Path(CHROME).exists():
        raise SystemExit(f'PDF návodů a náhledy pro sdílení potřebují Google Chrome ({CHROME})')
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(TichyServer, directory=VYSTUP))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with tempfile.TemporaryDirectory() as profil:
            def spust(cesta, *volby):
                subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={profil}',
                                '--virtual-time-budget=10000', *volby, f'http://127.0.0.1:{server.server_port}{cesta}'],
                               check=True, capture_output=True)
            yield spust
    finally:
        server.shutdown()


def vytvor_pdf(lekce):
    """Vytiskne stránky lekcí do PDF přes Chrome bez okna. Vzhled tisku je v @media print ve styles.css."""
    pocty = {}
    with chrome() as spust:
        for l in lekce:
            cil = VYSTUP / l['adresa'] / nazev_pdf(l)
            spust(f'/{l["adresa"]}/', '--no-pdf-header-footer', f'--print-to-pdf={cil}')
            pocty[l['adresa']] = len(re.findall(rb'/Type\s*/Page[^s]', cil.read_bytes()))
    return pocty


# --- náhledy pro sdílení na sociálních sítích, 1200 × 630 jako u Facebooku ---

SDILENI = """<!doctype html>
<html lang="cs"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&display=swap">
<link rel="stylesheet" href="/styles.css">
<style>
html, body { margin: 0; width: 1200px; height: 630px; overflow: hidden; }
.karta { position: relative; display: grid; grid-template-columns: 1fr 500px; height: 630px; }
.text { padding: 56px 48px 96px 72px; display: flex; flex-direction: column; justify-content: center; }
h1 { font-size: 104px; font-weight: 800; font-stretch: 78%; font-variation-settings: "wdth" 78; line-height: 0.92;
  letter-spacing: -0.012em; margin: 0 0 28px; text-wrap: balance; }
h1 span { display: block; }
h1 span + span { color: var(--blue); }
.text p { font-size: 30px; line-height: 1.35; margin: 0; color: var(--ink-soft); }
.text .lesson-no { font-size: 28px; gap: 16px; margin: 0 0 22px; color: var(--ink-soft); }
.lesson-no .blob { width: 64px; height: 56px; font-size: 30px; }
.web { position: absolute; left: 72px; bottom: 44px; font-size: 24px; font-weight: 700; }
.web::before { content: ""; display: inline-block; width: 14px; height: 14px; border-radius: 50%; background: var(--pink); margin-right: 12px; }
.obraz { overflow: hidden; }
.obraz img { width: 100%; height: 100%; object-fit: cover; }
.obraz.nakres { background: var(--paper); display: grid; place-items: center; padding: 32px; }
.obraz .diagram { margin: 0; padding: 0; max-width: none; width: 100%; }
.obraz figcaption { display: none; }
.obraz .tower { display: block; max-width: none; width: auto; height: 590px; margin: 30px auto 0; }
.tower .s, .tower .b, .tower .top { animation: none; stroke-dashoffset: 0; scale: 1; }
</style></head><body>
<div class="karta">
<div class="text">{text}</div>
<div class="obraz{trida}">{obraz}</div>
<div class="web">bastleni.oram.cz</div>
</div>
</body></html>"""


def obrazek_sdileni(jmeno):
    # otisk obsahu v adrese, jinak Facebook ukazuje starý obrázek ze své mezipaměti
    otisk = hashlib.md5((VYSTUP / 'sdileni' / f'{jmeno}.jpg').read_bytes()).hexdigest()[:8]
    return f'{WEB}/sdileni/{jmeno}.jpg?v={otisk}'


def vytvor_nahledy(lekce, domu):
    """Vyfotí karty pro sdílení v Chromu bez okna a uloží je jako sdileni/*.jpg."""
    karty = {'domu': ('<h1><span>Bastlířská</span><span>dílna</span></h1>' f'<p>{domu["perex"]}</p>', vez(), '')}
    for l in lekce:
        if 'prehled_fotky' in l:
            obraz, trida = f'<img src="/foto/{l["prehled_fotky"].split()[0]}" alt="">', ''
        else:
            obraz, trida = NAKRESY[l['prehled_nakres']], ' nakres'
        karty[l['adresa']] = (cislo(l) + f'<h1>{l["nazev"]}</h1><p>{l["popis"]}</p>', obraz, trida)
    slozka = VYSTUP / 'sdileni'
    slozka.mkdir()
    with chrome() as spust:
        for jmeno, (text, obraz, trida) in karty.items():
            html, png = slozka / f'{jmeno}.html', slozka / f'{jmeno}.png'
            html.write_text(SDILENI.replace('{text}', text).replace('{obraz}', obraz).replace('{trida}', trida))
            spust(f'/sdileni/{jmeno}.html', '--window-size=1200,630', f'--screenshot={png}')
            subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '85', png, '--out', slozka / f'{jmeno}.jpg'],
                           check=True, capture_output=True)
            png.unlink()
            html.unlink()


def zapis_lekce(lekce, pocty=None):
    for i, l in enumerate(lekce):
        predchozi = lekce[i - 1] if i > 0 else None
        dalsi = lekce[i + 1] if i + 1 < len(lekce) else None
        (VYSTUP / l['adresa']).mkdir(exist_ok=True)
        html = stranka_lekce(l, predchozi, dalsi, (pocty or {}).get(l['adresa']))
        (VYSTUP / l['adresa'] / 'index.html').write_text(html)


def main():
    s_koncepty = '--koncepty' in sys.argv
    dnes = datetime.date.today()
    lekce = []
    for soubor in sorted((ZDROJ / 'lekce').glob('*.md')):
        meta, telo = nacti(soubor)
        l = meta | {'telo': telo, 'cislo': int(soubor.name.split('-')[0])}
        if 'zverejnit' in l:
            l['zverejnit'] = datetime.date.fromisoformat(l['zverejnit'])
            l['koncept'] = l['zverejnit'] > dnes
        if l.get('koncept') and not s_koncepty:
            print(f'Koncept {soubor.name} vynechán, zveřejní se {l["zverejnit"]}')
            continue
        lekce.append(l)

    shutil.rmtree(VYSTUP, ignore_errors=True)
    shutil.copytree(ZDROJ / 'static', VYSTUP, ignore=shutil.ignore_patterns('.DS_Store'))
    vytvor_nahledy(lekce, nacti(ZDROJ / 'domu.md')[0])
    (VYSTUP / 'index.html').write_text(stranka_domu(lekce))
    # dvakrát: PDF se tiskne z hotové stránky a tlačítko pak potřebuje znát počet stran
    zapis_lekce(lekce)
    zapis_lekce(lekce, vytvor_pdf(lekce))
    print(f'Hotovo: {VYSTUP} ({len(lekce)} lekcí)')


if __name__ == '__main__':
    main()
