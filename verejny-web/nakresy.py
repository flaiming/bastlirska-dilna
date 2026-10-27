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
    + sipka_dolu(275, 18, 42) + spag((275, 170), (275, 114)) + spag((275, 106), (275, 50)) + paska(268, 96, 14, 28)
    + '<text class="lbl" x="75" y="192" text-anchor="middle">jedna se ohne</text>'
    + '<text class="lbl" x="170" y="192" text-anchor="middle">svazek</text>'
    + '<text class="lbl" x="275" y="192" text-anchor="middle">spoj v půlce</text>',
    'Jedna dlouhá špageta se pod zátěží ohne, svazek nebo spoj v půlce vydrží'),
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
