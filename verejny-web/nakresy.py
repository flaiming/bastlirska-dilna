# Schematické nákresy ke krokům návodů. V Markdownu se vkládají řádkem {{nakres jmeno}}.
import math

KAR = 'fill="#DDBB86" stroke="#9C7442" stroke-width="1.5"'
SPEJLE = '#C49A5E'
def dim_h(x1, x2, y, label):
    return (f'<g class="dim"><line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>'
            f'<line x1="{x1}" y1="{y-5}" x2="{x1}" y2="{y+5}"/><line x1="{x2}" y1="{y-5}" x2="{x2}" y2="{y+5}"/></g>'
            f'<text class="lbl" x="{(x1+x2)/2}" y="{y-6}" text-anchor="middle">{label}</text>')
def dim_v(x, y1, y2, label):
    return (f'<g class="dim"><line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}"/>'
            f'<line x1="{x-5}" y1="{y1}" x2="{x+5}" y2="{y1}"/><line x1="{x-5}" y1="{y2}" x2="{x+5}" y2="{y2}"/></g>'
            f'<text class="lbl" x="{x-8}" y="{(y1+y2)/2+4}" text-anchor="end">{label}</text>')
def note(x1, y1, x2, y2, label, anchor="start"):
    tx = x2 + (4 if anchor == "start" else -4 if anchor == "end" else 0)
    ty = y2 + 4 if anchor != "middle" else (y2 + 12 if y2 > y1 else y2 - 4)
    return (f'<line class="lead" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/><circle class="dot" cx="{x1}" cy="{y1}" r="2.5"/>'
            f'<text class="lbl" x="{tx}" y="{ty}" text-anchor="{anchor}">{label}</text>')
def glue(x1, y1, x2, y2, pad=3.5, amp=1.6, step=2.0):
    # vlnitý obrys tavného lepidla po celém obvodu dílu
    x1, y1, x2, y2 = x1 - pad, y1 - pad, x2 + pad, y2 + pad
    w, h = x2 - x1, y2 - y1
    per = 2 * (w + h)
    pts = []
    t = 0.0
    while t < per:
        if t < w: x, y, nx, ny = x1 + t, y1, 0, -1
        elif t < w + h: x, y, nx, ny = x2, y1 + t - w, 1, 0
        elif t < 2 * w + h: x, y, nx, ny = x2 - (t - w - h), y2, 0, 1
        else: x, y, nx, ny = x1, y2 - (t - 2 * w - h), -1, 0
        o = amp * math.sin(t / 2.2)
        pts.append(f'{x + nx * o:.1f},{y + ny * o:.1f}')
        t += step
    return f'<polygon points="{" ".join(pts)}" fill="#EEF5FA" stroke="#93A9BF" stroke-width="1.1" stroke-linejoin="round"/>'
def old(*parts): return '<g class="old">' + ''.join(parts) + '</g>'

# --- podvozek (shora i zespodu vypadá stejně, výřez je vzadu) ---
chassis = f'<path d="M60 60 H260 V85 H230 V115 H260 V140 H60 Z" {KAR}/>'
ends = '<text class="hint" x="70" y="104">předek</text><text class="hint" x="222" y="104" text-anchor="end">zadek</text>'
def straw(x, y1, y2):
    # lepidlo jen tam, kde je pod brčkem karton (y 60–85 a 115–140 vzadu, 60–140 vpředu)
    gy1, gy2 = max(y1, 60) + 3.5, min(y2, 140) - 3.5
    if y2 <= 86: gy2 = 85 - 3.5
    if y1 >= 114: gy1 = 115 + 3.5
    return (glue(x - 5, gy1, x + 5, gy2)
            + f'<rect x="{x-5}" y="{y1}" width="10" height="{y2-y1}" rx="2" fill="#E6EEFB" stroke="#2F6FE0" stroke-width="1.5"/>')
straws = straw(85, 58, 142) + straw(245, 58, 86) + straw(245, 114, 142)
def wheels(x, d):
    return (f'<rect x="{x-d/2}" y="44" width="{d}" height="11" rx="3" fill="#1B2B4B"/>'
            f'<rect x="{x-d/2}" y="145" width="{d}" height="11" rx="3" fill="#1B2B4B"/>')
def axle(x):
    return f'<line x1="{x}" y1="38" x2="{x}" y2="162" stroke="{SPEJLE}" stroke-width="3.5" stroke-linecap="round"/>'
axles = axle(85) + axle(245) + wheels(85, 30) + wheels(245, 42)
# pohled shora: osy jsou pod kartonem, zadní je vidět ve výřezu
top_base = axle(85) + axle(245) + chassis + wheels(85, 30) + wheels(245, 42)
hook = (f'<line x1="36" y1="100" x2="60" y2="100" stroke="{SPEJLE}" stroke-width="3.5" stroke-linecap="round"/>'
        f'<line x1="60" y1="100" x2="88" y2="100" stroke="{SPEJLE}" stroke-width="2" stroke-dasharray="3 3"/>')
pin = glue(242, 96, 248, 104, pad=1.5, amp=0.8) + f'<rect x="237" y="97" width="16" height="6" rx="2" fill="{SPEJLE}"/>'
band = ('<rect x="56" y="96" width="84" height="8" rx="4" fill="none" stroke="#E8487A" stroke-width="2.5"/>'
        '<rect x="134" y="95" width="116" height="10" rx="5" fill="none" stroke="#C93A66" stroke-width="2.5"/>')

# --- detail zarážky ve výřezu, zvětšeno ---
detail_base = ('<line x1="170" y1="0" x2="170" y2="200" stroke="#C49A5E" stroke-width="10" stroke-linecap="round"/>'
               f'<path d="M20 8 H230 V45 H110 V155 H230 V192 H20 Z" {KAR}/>'
               '<text class="hint" x="40" y="104">karton</text>')
# lepidlo pod zarážkou, jen ve styku s osou
detail_pin = (glue(162, 92, 178, 108, pad=3, amp=1.6)
              + '<rect x="140" y="94" width="60" height="12" rx="3" fill="#C49A5E" stroke="#9C7442" stroke-width="1"/>')
detail_thread = '<path d="M158 88 L182 112 M182 88 L158 112 M161 86 L185 110" stroke="#1B2B4B" stroke-width="1.6" stroke-linecap="round"/>'

# --- pohled z boku ---
def wheel(cx, cy, r):
    sp = ''.join(f'<line x1="{cx}" y1="{cy}" x2="{cx + r*c:.1f}" y2="{cy + r*s:.1f}"/>'
                 for c, s in [(1,0),(-1,0),(.5,.866),(-.5,-.866),(.5,-.866),(-.5,.866)])
    return (f'<g stroke="#D98C9A" stroke-width="2">{sp}</g>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1B2B4B" stroke-width="4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="#1B2B4B"/>')
side_car = ('<line x1="60" y1="134" x2="262" y2="126" stroke="#DDBB86" stroke-width="7"/>'
            f'<line x1="46" y1="134.5" x2="62" y2="134" stroke="{SPEJLE}" stroke-width="3" stroke-linecap="round"/>'
            + wheel(85, 146, 14) + wheel(245, 140, 20))
side_band = ('<path d="M61 131.5 L230 122.5 L243 136" fill="none" stroke="#E8487A" stroke-width="2.5" stroke-linejoin="round"/>'
             '<circle cx="245" cy="140" r="5.5" fill="none" stroke="#E8487A" stroke-width="3"/>')
ground = '<line class="ground" x1="20" y1="160" x2="320" y2="160"/>'

ARROW = ('<defs><marker id="sip{n}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         '<path d="M0 0 L10 5 L0 10 z" fill="#1B2B4B"/></marker></defs>')

def svg(n, body, label, vb='0 0 340 200'):
    return (f'<figure class="diagram"><svg viewBox="{vb}" role="img" aria-label="{label}">'
            + ARROW.format(n=n) + body.replace('{n}', str(n)) + '</svg>'
            f'<figcaption>{label}</figcaption></figure>')

NAKRESY = {
 'podvozek': svg(1,
    chassis + ends + dim_h(60, 260, 40, '20 cm') + dim_v(42, 60, 140, '8 cm')
    + note(245, 108, 290, 178, 'výřez 3 × 3 cm', 'end'),
    'Podvozek s výřezem vzadu uprostřed'),
 'brcka': svg(2,
    old(chassis) + straws + dim_h(85, 245, 44, 'stejně daleko') + dim_h(85, 245, 166, 'jako tady')
    + note(245, 100, 262, 22, 'střed volný'),
    'Pohled zespodu: vpředu jedno brčko, vzadu dva kousky vedle výřezu'),
 'kola': svg(3,
    old(chassis, straws) + axles
    + note(226, 153, 196, 186, 'větší zadní kola', 'end') + note(88, 57, 140, 20, 'jen malá mezera'),
    'Pohled zespodu: špejle v brčkách, na koncích kola'),
 'hacek': svg(4,
    old(top_base) + hook + note(44, 100, 70, 188, 'kousek špejle zasunutý do kartonu', 'start'),
    'Pohled shora: háček ze špejle v přední hraně kartonu'),
 'zarazka': svg(5,
    old(detail_base) + detail_pin + detail_thread
    + note(196, 100, 234, 66, 'zarážka 1–1,5 cm')
    + note(180, 110, 234, 132, 'přilepit a přivázat')
    + note(170, 176, 234, 176, 'zadní osa'),
    'Detail výřezu shora: zarážka přilepená napříč přes střed zadní osy'),
 'gumicka': svg(6,
    old(top_base, hook, pin) + band
    + note(137, 104, 150, 186, '2–3 gumičky za sebou', 'middle'),
    'Pohled shora: gumička od háčku po kartonu na zarážku, ani volná, ani napnutá'),
 'natoceni': svg(7,
    ground + old(side_car) + side_band
    + '<path d="M217 124 A32 32 0 0 1 273 124" fill="none" stroke="#1B2B4B" stroke-width="2.5" marker-end="url(#sip{n})"/>'
    + '<text class="lbl" x="245" y="84" text-anchor="middle">točit dozadu 5–10×</text>'
    + '<line x1="200" y1="182" x2="90" y2="182" stroke="#1B2B4B" stroke-width="2.5" marker-end="url(#sip{n})"/>'
    + '<text class="lbl" x="208" y="186">pak auto pojede sem</text>',
    'Pohled z boku: natočením zadních kol se gumička navine na osu', '0 68 340 128'),
 'mereni': svg(8,
    '<line class="ground" x1="20" y1="160" x2="320" y2="160"/>'
    + '<g transform="translate(-10 80) scale(.5)">' + side_car + side_band + '</g>'
    + '<line x1="300" y1="110" x2="300" y2="166" stroke="#1B2B4B" stroke-width="2" stroke-dasharray="5 4"/>'
    + '<text class="lbl" x="300" y="102" text-anchor="middle">start</text>'
    + '<line x1="20" y1="140" x2="20" y2="186" stroke="#1B2B4B" stroke-width="1.2" stroke-dasharray="3 3"/>'
    + '<g class="dim"><line x1="20" y1="182" x2="300" y2="182"/>'
    + ''.join(f'<line x1="{x}" y1="178" x2="{x}" y2="186"/>' for x in range(20, 301, 35)) + '</g>'
    + '<text class="lbl" x="230" y="176" text-anchor="middle">dojezd</text>'
    + '<g stroke="#9AA6B8" stroke-width="2" stroke-linecap="round"><line x1="150" y1="130" x2="180" y2="130"/><line x1="146" y1="140" x2="186" y2="140"/><line x1="152" y1="150" x2="172" y2="150"/></g>',
    'Změřte, jak daleko auto dojelo od startu', '0 88 340 108'),
}



# --- věž ze špaget: obecné zásady stavby, ne hotový návrh, ať zbude prostor pro vlastní nápady ---
def spag(*body, barva='#E9B425', sirka=4):
    """Lomená čára ze špaget přes zadané body."""
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in body)
    return f'<path d="{d}" fill="none" stroke="{barva}" stroke-width="{sirka}" stroke-linecap="round" stroke-linejoin="round"/>'
def kulicka(x, y, barva, r=7):
    return f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r - 1}" fill="{barva}"/>'
def kulicky(body, barvy=('#E8487A', '#2F6FE0', '#13A39A', '#F08A24')):
    return ''.join(kulicka(x, y, barvy[i % len(barvy)]) for i, (x, y) in enumerate(body))
def paska(x, y, w, h=7):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5" fill="#EEF5FA" fill-opacity=".45" stroke="#93A9BF" stroke-width="1.1"/>'
def sipka_dolu(x, y1, y2):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="#1B2B4B" stroke-width="2.5" marker-end="url(#sip{{n}})"/>'
stul = '<line class="ground" x1="20" y1="170" x2="320" y2="170"/>'

troj = [(40, 160), (140, 160), (90, 73)]
ctverec = [(205, 75), (295, 75), (295, 160), (205, 160)]
kosoctverec = [(40, 150), (130, 150), (160, 60), (70, 60)]

NAKRESY.update({
 'vez-zaklad': svg(11,
    spag(*troj, troj[0]) + kulicky(troj) + spag(*ctverec, ctverec[0]) + kulicky(ctverec)
    + '<text class="lbl" x="90" y="190" text-anchor="middle">trojúhelník</text>'
    + '<text class="lbl" x="250" y="190" text-anchor="middle">nebo čtverec</text>'
    + note(295, 75, 250, 34, 'kulička plastelíny obalí konce špaget', 'end'),
    'Základna shora: špagety spojené v rozích kuličkami plastelíny'),
 'vez-steny': svg(12,
    old(spag(*kosoctverec[:2], (130, 60), (40, 60), kosoctverec[0]))
    + spag(*kosoctverec, kosoctverec[0]) + kulicky(kosoctverec)
    + '<line x1="22" y1="60" x2="58" y2="60" stroke="#1B2B4B" stroke-width="2.5" marker-end="url(#sip{n})"/>'
    + spag((300, 150), (210, 150), (210, 60), (300, 60), (300, 150), (210, 60))
    + kulicky([(210, 150), (300, 150), (300, 60), (210, 60)])
    + '<line x1="176" y1="60" x2="198" y2="60" stroke="#1B2B4B" stroke-width="2.5" marker-end="url(#sip{n})"/>'
    + note(255, 105, 290, 30, 'šikmá špageta', 'end')
    + '<text class="lbl" x="95" y="185" text-anchor="middle">bez šikmé se zkroutí</text>'
    + '<text class="lbl" x="255" y="185" text-anchor="middle">se šikmou drží</text>',
    'Stěna z boku: čtverec se po zatlačení zkřiví, s šikmou špagetou drží tvar'),
 'vez-svazek': svg(13,
    stul
    + sipka_dolu(75, 18, 42) + '<path d="M75 170 Q100 110 75 50" fill="none" stroke="#E9B425" stroke-width="4" stroke-linecap="round"/>'
    + sipka_dolu(170, 18, 42) + spag((165, 170), (165, 50)) + spag((170, 170), (170, 50)) + spag((175, 170), (175, 50))
    + paska(161, 74, 18, 14) + paska(161, 132, 18, 14)
    + '<line x1="225" y1="30" x2="225" y2="176" stroke="#9AA6B8" stroke-width="1.2" stroke-dasharray="4 4"/>'
    + spag((272, 170), (272, 84)) + spag((278, 136), (278, 50)) + paska(268, 88, 14, 12) + paska(268, 120, 14, 12)
    + '<text class="lbl" x="75" y="192" text-anchor="middle">jedna se ohne</text>'
    + '<text class="lbl" x="170" y="192" text-anchor="middle">svazek drží</text>'
    + '<text class="lbl" x="275" y="192" text-anchor="middle">prodloužení</text>',
    'Jedna dlouhá špageta se pod zátěží ohne, svazek vydrží. Delší kus vznikne překrytím dvou špaget a páskou.'),
 'vez-mereni': svg(14,
    '<line class="ground" x1="20" y1="175" x2="320" y2="175"/>'
    + old(spag((110, 175), (150, 55), (190, 55), (230, 175), (110, 175)),
          spag((123, 135), (217, 135)), spag((137, 95), (203, 95)),
          spag((110, 175), (217, 135), (137, 95), (190, 55)),
          kulicky([(110, 175), (230, 175), (123, 135), (217, 135), (137, 95), (203, 95), (150, 55), (190, 55)]))
    + '<text class="hint" x="170" y="193" text-anchor="middle">tvar věže je na vás</text>'
    + '<path d="M155 25 L185 25 L181 50 L159 50 Z" fill="#F4F7FA" stroke="#1B2B4B" stroke-width="2" stroke-linejoin="round"/>'
    + dim_v(70, 55, 175, 'výška') + '<line class="lead" x1="70" y1="55" x2="146" y2="55" stroke-dasharray="3 3"/>'
    + note(183, 36, 236, 24, 'zátěž navrch'),
    'Výška se měří od stolu po vrchol, zátěž se položí na nejvyšší bod'),
})


# --- věž ze špaget v úvodu webu ---
def vez():
    """Věž s rovnou horní plošinou, na které stojí kelímek s hřebíky. Metr měří výšku po plošinu."""
    zem, vrch, cm = 540, 60, 112          # vrch = horní plošina, ta měří 112 cm
    px = (zem - vrch) / cm                # pixelů na centimetr
    # patra: mezery se směrem nahoru zmenšují, šířka se zužuje rovnoměrně
    mezery = [96 * 0.93 ** k for k in range(6)]
    mezery = [m * (zem - vrch) / sum(mezery) for m in mezery]
    patra, y = [], zem
    for m in [0] + mezery:
        y -= m
        patra.append((round(y), round(26 + 109 * (y - vrch) / (zem - vrch))))
    body = [((200 - w, y), (200 + w, y)) for y, w in patra]

    cary = []
    def cara(a, b):
        cary.append(f'<line class="s" style="--i:{len(cary)}" x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" pathLength="1"/>')
    for k, (l, r) in enumerate(body):
        cara(l, r)
        if k + 1 < len(body):
            l2, r2 = body[k + 1]
            cara(l, l2)
            cara(r, r2)
            cara(l, r2) if k % 2 == 0 else cara(r, l2)

    barvy = ['#E8487A', '#2F6FE0', '#2F6FE0', '#F08A24', '#E8487A', '#13A39A', '#F08A24',
             '#13A39A', '#E0402B', '#13A39A', '#13A39A', '#2F6FE0', '#E0402B', '#2F6FE0']
    spoje = []
    for k, (l, r) in enumerate(body):
        for j, (x, y) in enumerate((l, r)):
            rx = 8 + (k + j) % 3
            spoje.append(f'<ellipse class="b" style="--i:{k}" cx="{x}" cy="{y}" rx="{rx}" ry="{rx - 1 - j}" fill="{barvy[2 * k + j]}"/>')

    metr = [f'<line x1="408" y1="{zem}" x2="408" y2="{vrch}"/>']
    for d in range(0, cm - 5, 10):
        sirka = 10 if d % 50 == 0 else 6
        metr.append(f'<line x1="{408 - sirka}" y1="{zem - d * px:.0f}" x2="{408 + sirka}" y2="{zem - d * px:.0f}"/>')
    metr.append(f'<line x1="398" y1="{vrch}" x2="418" y2="{vrch}"/>')
    popisky = ''.join(f'<text class="ruler-note" x="392" y="{zem - d * px + 4:.0f}" text-anchor="end">{d}</text>' for d in (50, 100))

    # kelímek stojí na plošině
    dno = vrch - 3
    kelimek = (f'<g class="top"><g stroke="#7A8696" stroke-width="2.5" stroke-linecap="round">'
               f'<line x1="193" y1="{dno - 20}" x2="188" y2="{dno - 40}"/><line x1="185" y1="{dno - 40}" x2="191" y2="{dno - 41}"/>'
               f'<line x1="200" y1="{dno - 20}" x2="201" y2="{dno - 43}"/><line x1="198" y1="{dno - 43}" x2="204" y2="{dno - 43}"/>'
               f'<line x1="207" y1="{dno - 20}" x2="213" y2="{dno - 38}"/><line x1="210" y1="{dno - 39}" x2="216" y2="{dno - 37}"/></g>'
               f'<path d="M182 {dno - 30} L218 {dno - 30} L213 {dno} L187 {dno} Z" fill="#F4F7FA" stroke="#1B2B4B" stroke-width="2" stroke-linejoin="round"/></g>')

    return ('<svg class="tower" viewBox="0 0 440 570" role="img" aria-labelledby="vez-popis">'
            f'<title id="vez-popis">Věž ze špaget spojených plastelínou, na horní plošině kelímek s hřebíky, vedle metr ukazující {cm} cm</title>'
            '<g class="ruler" aria-hidden="true">' + ''.join(metr) + '</g>'
            f'<text class="ruler-label" x="420" y="{vrch - 12}" text-anchor="end">{cm} cm</text>' + popisky
            + '\n'.join(cary) + '\n'.join(spoje) + kelimek + '</svg>')


# --- drátěný hlavolam a pájení ---
MED, MED_TMAVA = '#C9763A', '#8E4A1E'
CIN = '#B7C0CB'
PASKA = '#2E4A7A'
def med(d, sirka=4):
    return f'<path d="{d}" fill="none" stroke="{MED}" stroke-width="{sirka}" stroke-linecap="round" stroke-linejoin="round"/>'
def kabel(d, barva, sirka=4):
    return f'<path d="{d}" fill="none" stroke="{barva}" stroke-width="{sirka}" stroke-linecap="round" stroke-linejoin="round"/>'
def spoj(x, y, r=4.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{CIN}" stroke="#7D8794" stroke-width="1"/><circle cx="{x - r/3:.1f}" cy="{y - r/3:.1f}" r="{r/3:.1f}" fill="#fff"/>'
def izolepa(x, y, w, h):
    pruhy = ''.join(f'<line x1="{x + i}" y1="{y}" x2="{x + i + 3}" y2="{y + h}" stroke="#fff" stroke-opacity=".35" stroke-width="1"/>'
                    for i in range(3, int(w) - 2, 5))
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{PASKA}"/>' + pruhy

draha = 'M70 170 V128 C70 98 98 88 114 102 C130 116 128 134 148 132 C170 130 168 92 192 92 C214 92 210 122 228 120 C248 118 256 92 242 90 C228 88 230 116 252 118 C268 120 270 112 270 128 V170'
hlavolam = (
    f'<rect x="40" y="170" width="260" height="16" rx="3" {KAR}/>'
    + '<text class="hint" x="282" y="181" text-anchor="end">prkýnko</text>'
    # baterie a bzučák přilepené na prkýnku
    + f'<rect x="84" y="150" width="62" height="20" rx="3" fill="#3B4A63"/><rect x="146" y="155" width="4" height="10" fill="#3B4A63"/>'
    + '<text x="115" y="164" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">2× AA</text>'
    + '<rect x="170" y="152" width="22" height="18" rx="3" fill="#1B2B4B"/><text x="181" y="165" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">+</text>'
    + med(draha) + izolepa(65, 128, 10, 28) + izolepa(265, 128, 10, 28)
    + kabel('M150 160 C158 160 160 166 172 166', '#E0402B', 3)
    + kabel('M190 166 C220 166 240 165 266 165', '#13A39A', 3) + spoj(269, 165, 3.5)
    # očko na dráze, rukojeť nahoru, lanko k baterii
    + f'<ellipse cx="192" cy="92" rx="5" ry="13" fill="none" stroke="{MED_TMAVA}" stroke-width="3"/>'
    + med('M192 80 L196 30', 3) + izolepa(191, 30, 10, 34)
    + kabel('M196 30 C200 6 120 4 60 40 C20 64 30 150 84 160', '#E9B425', 3)
    + note(70, 142, 22, 120, 'start', 'end') + note(270, 142, 318, 120, 'cíl')
    + note(115, 108, 120, 62, 'dráha', 'middle') + note(201, 46, 236, 34, 'očko s rukojetí')
    + note(181, 152, 214, 140, 'bzučák')
)

NAKRESY.update({
 'hlavolam': svg(21, hlavolam,
    'Hotový hlavolam: dráha je zastrčená v prkýnku, na koncích izolepa. Baterie, bzučák a očko jsou spojené lanky.',
    '0 0 340 196'),
 'pajeni-postup': svg(22,
    # drát upnutý vlevo, páječka zprava shora, cín zleva zdola
    kabel('M20 130 H122', '#2F6FE0', 9) + med('M120 130 H196', 4)
    + '<path d="M18 116 L58 124 L58 136 L18 144 Z" fill="#7A8696"/><text class="hint" x="20" y="162">třetí ruka</text>'
    + '<g transform="translate(173 128) rotate(-36)">'
    + '<path d="M0 0 L28 -4 L28 4 Z" fill="#8A939F"/><rect x="28" y="-3" width="62" height="6" fill="#B9C1CB"/>'
    + '<rect x="86" y="-6" width="10" height="12" rx="2" fill="#5B6577"/><rect x="96" y="-9" width="84" height="18" rx="8" fill="#1B2B4B"/></g>'
    + f'<path d="M166 135 C162 158 158 182 155 206" fill="none" stroke="{CIN}" stroke-width="3" stroke-linecap="round"/>'
    + f'<ellipse cx="169" cy="131" rx="7" ry="4" fill="{CIN}"/><ellipse cx="167" cy="130" rx="2" ry="1" fill="#fff"/>'
    + note(178, 124, 228, 150, 'hrot ohřívá drát') + note(161, 166, 140, 176, 'cín přikládej k drátu,', 'end')
    + '<text class="lbl" x="136" y="194" text-anchor="end">ne na hrot</text>',
    'Hrot ohřívá drát shora, cín se přikládá z druhé strany k drátu a roztaví se jeho teplem.', '0 20 340 186'),
})

def zkrut(x, y, w=26):
    """Dva zkroucené drátky, konce v izolaci."""
    a = f'M{x - w} {y} ' + ' '.join(f'Q{x - w + 6.5 + 13 * i} {y + (-5 if i % 2 else 5)} {x - w + 13 * (i + 1)} {y}' for i in range(4))
    b = f'M{x - w} {y} ' + ' '.join(f'Q{x - w + 6.5 + 13 * i} {y + (5 if i % 2 else -5)} {x - w + 13 * (i + 1)} {y}' for i in range(4))
    return (kabel(f'M{x - 46} {y} H{x - w - 4}', '#2F6FE0', 9) + kabel(f'M{x + w + 4} {y} H{x + 46}', '#E0402B', 9)
            + med(f'M{x - w - 6} {y} H{x - w}', 3) + med(f'M{x + w} {y} H{x + w + 6}', 3) + med(a, 3) + med(b, 3))

def popisek(x, y, *radky, znak='', barva='#1B2B4B'):
    t = f'<text class="lbl" x="{x}" y="{y}" text-anchor="middle" style="fill:{barva};font-size:14px">{znak}</text>' if znak else ''
    return t + ''.join(f'<text class="lbl" x="{x}" y="{y + 18 + 14 * i}" text-anchor="middle">{r}</text>' for i, r in enumerate(radky))

hrbolky = ' '.join(f'{170 + (12 + (2.5 if i % 2 else 0)) * math.cos(i * math.pi / 7):.1f},{78 + (11 + (2.5 if i % 2 else 0)) * math.sin(i * math.pi / 7):.1f}' for i in range(14))
NAKRESY.update({
 'pajeni-spoj': svg(23,
    zkrut(57, 80)
    + f'<path d="M27 80 Q35 72 57 73 Q79 72 87 80 Q79 88 57 87 Q35 88 27 80 Z" fill="{CIN}" fill-opacity=".8" stroke="#8D97A3" stroke-width="1"/>'
    + med('M33 80 Q40 76 47 80 Q54 84 61 80 Q68 76 75 80 Q78 82 81 80', 1.5).replace(MED, '#8D97A3')
    + '<path d="M38 76 Q57 73 76 76" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>'
    + popisek(57, 122, 'lesklý a hladký,', 'zatekl mezi dráty', znak='✓ dobře', barva='#13A39A')
    + zkrut(170, 80)
    + f'<polygon points="{hrbolky}" fill="#8F969E" stroke="#6E747B" stroke-width="1" stroke-linejoin="round"/>'
    + '<path d="M164 72 l4 5 M175 80 l-3 4 M168 86 l5 -2" stroke="#6E747B" stroke-width="1"/>'
    + popisek(170, 122, 'matná kulička,', 'drát byl studený', znak='✗ studený spoj', barva='#E8487A')
    + zkrut(283, 80)
    + f'<circle cx="283" cy="78" r="19" fill="{CIN}" stroke="#8D97A3" stroke-width="1"/><ellipse cx="276" cy="70" rx="6" ry="4" fill="#fff" fill-opacity=".85"/>'
    + popisek(283, 122, 'velká koule,', 'stačí kapka', znak='✗ moc cínu', barva='#E8487A'),
    'Dva zkroucené drátky po zapájení: dobrý spoj, studený spoj a spoj s moc cínu.', '0 50 340 112'),
 'ocko': svg(24,
    f'<path d="M128 85 A28 28 0 1 0 114 109.2" fill="none" stroke="{MED}" stroke-width="4" stroke-linecap="round"/>'
    + med('M128 85 H262') + izolepa(150, 79, 100, 12)
    + kabel('M262 85 C282 85 292 110 304 128', '#E9B425', 4) + spoj(262, 85, 4)
    + dim_v(62, 57, 113, '1,5–2 cm')
    + note(117, 103, 140, 126, 'mezera, aby šlo očko')
    + '<text class="lbl" x="144" y="144">nasadit na dráhu</text>'
    + note(200, 85, 200, 52, 'rukojeť omotaná izolepou', 'middle') + note(262, 85, 300, 52, 'lanko', 'middle'),
    'Očko ohnuté kolem fixy, s mezerou. Rukojeť je omotaná izolepou, na konci je připájené lanko.', '0 30 340 124'),
 'zapojeni': svg(25,
    # držák shora: dva články vedle sebe, vývody vpravo
    '<rect x="24" y="56" width="128" height="88" rx="6" fill="#3B4A63"/>'
    + ''.join(f'<rect x="34" y="{y}" width="104" height="30" rx="5" fill="#E9B425"/><rect x="34" y="{y}" width="26" height="30" rx="5" fill="#1B2B4B"/>' for y in (64, 106))
    + '<text x="100" y="84" text-anchor="middle" font-size="11" font-weight="700" fill="#1B2B4B">AA</text>'
    + '<text x="100" y="126" text-anchor="middle" font-size="11" font-weight="700" fill="#1B2B4B">AA</text>'
    + '<rect x="152" y="74" width="10" height="6" fill="#9AA6B8"/><rect x="152" y="120" width="10" height="6" fill="#9AA6B8"/>'
    + '<text class="lbl" x="166" y="72" style="font-size:15px">+</text><text class="lbl" x="166" y="140" style="font-size:15px">−</text>'
    # bzučák z boku: delší nožka je plus
    + '<rect x="196" y="20" width="40" height="26" rx="4" fill="#1B2B4B"/><text x="206" y="38" font-size="12" font-weight="700" fill="#fff">+</text>'
    + '<line x1="206" y1="46" x2="206" y2="86" stroke="#9AA6B8" stroke-width="2.5"/><line x1="226" y1="46" x2="226" y2="72" stroke="#9AA6B8" stroke-width="2.5"/>'
    + kabel('M162 77 C184 77 196 86 206 86', '#E0402B', 3.5) + spoj(162, 77) + spoj(206, 86)
    + kabel('M226 72 C250 72 270 84 300 84', '#13A39A', 3.5) + spoj(226, 72)
    + '<line x1="300" y1="84" x2="324" y2="84" stroke="#1B2B4B" stroke-width="2" marker-end="url(#sip{n})"/>'
    + '<text class="lbl" x="322" y="104" text-anchor="end">k dráze</text>'
    + kabel('M162 123 C200 123 240 150 300 150', '#E9B425', 3.5) + spoj(162, 123)
    + '<line x1="300" y1="150" x2="324" y2="150" stroke="#1B2B4B" stroke-width="2" marker-end="url(#sip{n})"/>'
    + '<text class="lbl" x="322" y="170" text-anchor="end">k očku</text>'
    + note(236, 33, 262, 33, 'bzučák') + note(206, 66, 186, 50, 'delší nožka +', 'end'),
    'Zapojení: plus baterie k delší nožce bzučáku, druhá nožka k dráze, mínus baterie dlouhým lankem k očku. Tečky jsou pájené spoje.',
    '0 8 340 172'),
})

# --- bonus: hlavolam s pamětí (samodržné relé), schéma v klidu ---
def sp(x1, x2, y, barva='#1B2B4B'):
    """Rozepnutý spínač ve schématu."""
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - 3}" y2="{y - 13}" stroke="{barva}" stroke-width="2.5" stroke-linecap="round"/>'
            f'<circle cx="{x1}" cy="{y}" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/>'
            f'<circle cx="{x2}" cy="{y}" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/>')
def vodic(body):
    return f'<polyline points="{body}" fill="none" stroke="#1B2B4B" stroke-width="2.5" stroke-linejoin="round"/>'
def uzel(x, y):
    return f'<circle cx="{x}" cy="{y}" r="3" fill="#1B2B4B"/>'
rele = (
    vodic('30,84 30,30 200,30') + '<circle cx="55" cy="30" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/><circle cx="85" cy="30" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/>' + vodic('200,30 305,30')
    + vodic('115,30 115,70 145,70') + vodic('170,70 200,70 200,30')
    + vodic('225,30 225,75') + vodic('225,105 225,150') + vodic('305,30 305,78') + vodic('305,108 305,150 30,150 30,112')
    # očko a dráha jako spínač v barvě mědi; přes ně je vodič přerušený
    + '<line x1="140" y1="30" x2="175" y2="30" stroke="#EDF1F4" stroke-width="5"/><rect x="140" y="26" width="35" height="8" fill="#fff"/>'
    + sp(145, 170, 30, MED) + sp(145, 170, 70)
    # baterie
    + '<g stroke="#1B2B4B" stroke-linecap="round"><line x1="18" y1="86" x2="42" y2="86" stroke-width="2.5"/><line x1="24" y1="93" x2="36" y2="93" stroke-width="4"/>'
    + '<line x1="18" y1="103" x2="42" y2="103" stroke-width="2.5"/><line x1="24" y1="110" x2="36" y2="110" stroke-width="4"/></g>'
    + '<line x1="30" y1="93" x2="30" y2="103" stroke="#1B2B4B" stroke-width="1.5" stroke-dasharray="2 2"/>'
    + '<text class="lbl" x="46" y="90">+</text><text class="lbl" x="30" y="128" text-anchor="middle">2× AA</text>'
    # cívka relé a vazba na kontakt
    + '<rect x="215" y="75" width="20" height="30" rx="2" fill="#fff" stroke="#2F6FE0" stroke-width="2.5"/><line x1="217" y1="103" x2="233" y2="77" stroke="#2F6FE0" stroke-width="1.2"/>'
    + '<polyline points="157,63 157,90 215,90" fill="none" stroke="#2F6FE0" stroke-width="1.5" stroke-dasharray="4 3"/>'
    # dioda proužkem k plusu
    + '<polyline points="262,30 262,82" fill="none" stroke="#1B2B4B" stroke-width="1.5"/><polyline points="262,96 262,150" fill="none" stroke="#1B2B4B" stroke-width="1.5"/>'
    + '<path d="M255 96 L269 96 L262 84 Z" fill="#1B2B4B"/><line x1="255" y1="83" x2="269" y2="83" stroke="#1B2B4B" stroke-width="2"/>'
    # bzučák
    + '<rect x="296" y="78" width="18" height="30" rx="3" fill="#fff" stroke="#1B2B4B" stroke-width="2.5"/><text class="lbl" x="300" y="90" style="font-size:10px">+</text>'
    + uzel(115, 30) + uzel(200, 30) + uzel(225, 30) + uzel(262, 30) + uzel(225, 150) + uzel(262, 150)
    + '<text class="lbl" x="70" y="14" text-anchor="middle">vypínač = reset</text>'
    + f'<text class="lbl" x="158" y="14" text-anchor="middle" style="fill:{MED_TMAVA}">očko ~ dráha</text>'
    + '<text class="lbl" x="140" y="90" text-anchor="end">kontakt relé</text>'
    + '<text class="hint" x="140" y="103" text-anchor="end">COM a NO</text>'
    + '<text class="lbl" x="218" y="121" text-anchor="end">cívka</text><text class="lbl" x="218" y="134" text-anchor="end">relé</text>'
    + '<text class="hint" x="262" y="140" text-anchor="middle">dioda</text>'
    + '<text class="lbl" x="305" y="124" text-anchor="middle">bzučák</text>'
)
NAKRESY['hlavolam-rele'] = svg(26, rele,
    'Schéma v klidu, vypínač je zapnutý. Kontakt relé je zapojený vedle očka a dráhy: když ho cívka přitáhne, vede proud místo nich.',
    '0 0 340 162')
