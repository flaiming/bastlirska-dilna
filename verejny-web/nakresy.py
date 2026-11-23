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
MEZERA = 2  # mezera mezi hrotem šipky popisku a místem, aby ho šipka nepřekryla
def note(x1, y1, x2, y2, label, anchor="start", odstup=MEZERA):
    tx = x2 + (4 if anchor == "start" else -4 if anchor == "end" else 0)
    ty = y2 + 4 if anchor != "middle" else (y2 + 12 if y2 > y1 else y2 - 4)
    # šipka vede od popisku k místu (x1, y1) a končí kousek před ním
    d = math.hypot(x2 - x1, y2 - y1) or 1
    sx, sy = x1 + (x2 - x1) * odstup / d, y1 + (y2 - y1) * odstup / d
    return (f'<line class="lead" x1="{x2}" y1="{y2}" x2="{sx:.1f}" y2="{sy:.1f}" marker-end="url(#hrot{{n}})"/>'
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
         '<path d="M0 0 L10 5 L0 10 z" fill="#1B2B4B"/></marker>'
         # malý hrot pro šipky popisků, velikost v px nezávislá na tloušťce čáry
         '<marker id="hrot{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="userSpaceOnUse" orient="auto">'
         '<path d="M0 1 L10 5 L0 9 z" fill="#1B2B4B"/></marker></defs>')

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
    + note(230, 157, 196, 186, 'větší zadní kola', 'end') + note(101, 57, 140, 20, 'jen malá mezera'),
    'Pohled zespodu: špejle v brčkách, na koncích kola'),
 'hacek': svg(4,
    old(top_base) + hook + note(44, 102, 70, 188, 'kousek špejle zasunutý do kartonu', 'start'),
    'Pohled shora: háček ze špejle v přední hraně kartonu'),
 'zarazka': svg(5,
    old(detail_base) + detail_pin + detail_thread
    + note(196, 93, 234, 66, 'zarážka 1–1,5 cm')
    + note(184, 114, 234, 132, 'přilepit a přivázat')
    + note(176, 176, 234, 176, 'zadní osa'),
    'Detail výřezu shora: zarážka přilepená napříč přes střed zadní osy'),
 'gumicka': svg(6,
    old(top_base, hook, pin) + band
    + note(138, 107, 150, 186, '2–3 gumičky za sebou', 'middle'),
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
    + note(295, 75, 250, 34, 'kulička plastelíny obalí konce špaget', 'end', odstup=10),
    'Základna shora: špagety spojené v rozích kuličkami plastelíny'),
 'vez-steny': svg(12,
    old(spag(*kosoctverec[:2], (130, 60), (40, 60), kosoctverec[0]))
    + spag(*kosoctverec, kosoctverec[0]) + kulicky(kosoctverec)
    + '<line x1="22" y1="60" x2="58" y2="60" stroke="#1B2B4B" stroke-width="2.5" marker-end="url(#sip{n})"/>'
    + spag((300, 150), (210, 150), (210, 60), (300, 60), (300, 150), (210, 60))
    + kulicky([(210, 150), (300, 150), (300, 60), (210, 60)])
    + '<line x1="176" y1="60" x2="198" y2="60" stroke="#1B2B4B" stroke-width="2.5" marker-end="url(#sip{n})"/>'
    + note(255, 105, 290, 30, 'šikmá špageta', 'end', odstup=5)
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
MODRA = '#2F6FE0'
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

CERNA, KOLEBKA = '#23272E', '#4A515C'
def vypinac_bok(x, y, w=22, h=14, nozicky=0):
    """Černý kolébkový vypínač z boku: tělo s límcem, nakloněná kolébka, vespod volitelně dva ploché kontakty."""
    k = (f'<rect x="{x + w * .25 - 2:.1f}" y="{y + h}" width="4" height="{nozicky}" fill="#9AA6B8"/>'
         f'<rect x="{x + w * .75 - 2:.1f}" y="{y + h}" width="4" height="{nozicky}" fill="#9AA6B8"/>') if nozicky else ''
    return (k + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{CERNA}"/>'
            f'<rect x="{x - 2}" y="{y}" width="{w + 4}" height="3" rx="1" fill="{CERNA}"/>'
            f'<path d="M{x + 3} {y} L{x + 3} {y - h * .3:.1f} L{x + w - 3} {y - h * .6:.1f} L{x + w - 3} {y} Z" fill="{KOLEBKA}"/>'
            f'<line x1="{x + w - 7}" y1="{y - h * .45:.1f}" x2="{x + w - 7}" y2="{y - h * .15:.1f}" stroke="#fff" stroke-width="1.2"/>')

draha = 'M70 170 V128 C70 98 98 88 114 102 C130 116 128 134 148 132 C170 130 168 92 192 92 C214 92 210 122 228 120 C248 118 256 92 242 90 C228 88 230 116 252 118 C268 120 270 112 270 128 V170'
hlavolam = (
    f'<rect x="40" y="170" width="260" height="16" rx="3" {KAR}/>'
    + '<text class="hint" x="282" y="181" text-anchor="end">prkénko</text>'
    # baterie a bzučák přilepené na prkénku
    + f'<rect x="80" y="150" width="56" height="20" rx="3" fill="#3B4A63"/><rect x="136" y="155" width="4" height="10" fill="#3B4A63"/>'
    + '<text x="108" y="164" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">2× AA</text>'
    + vypinac_bok(150, 156)
    + '<rect x="182" y="152" width="22" height="18" rx="3" fill="#1B2B4B"/><text x="188" y="165" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">+</text>'
    + med(draha) + izolepa(65, 128, 10, 28) + izolepa(265, 128, 10, 28)
    + kabel('M140 160 C145 160 146 164 150 164', '#E0402B', 3)
    + kabel('M172 164 C176 164 178 166 184 166', '#E0402B', 3)
    + kabel('M202 166 C226 166 244 165 266 165', '#E0402B', 3) + spoj(269, 165, 3.5)
    # očko na dráze, rukojeť nahoru, lanko k baterii
    + f'<ellipse cx="192" cy="92" rx="5" ry="13" fill="none" stroke="{MED_TMAVA}" stroke-width="3"/>'
    + med('M192 80 L196 30', 3) + izolepa(191, 30, 10, 34)
    + kabel('M196 30 C200 6 120 4 60 40 C20 64 30 150 80 160', MODRA, 3)
    + note(65, 140, 22, 120, 'start', 'end') + note(275, 140, 318, 120, 'cíl')
    + note(115, 108, 120, 62, 'dráha', 'middle', odstup=5) + note(201, 46, 236, 34, 'očko s rukojetí')
    + note(193, 152, 214, 140, 'bzučák')
    + note(161, 170, 161, 190, 'vypínač', 'middle')
)

def krokosvorka(x, y=130):
    """Krokosvorka shora zakousnutá do kabelu, střed kabelu v (x, y)."""
    zuby = ' '.join(f'L{x - 4 + 2 * i} {y + (9 if i % 2 else 7)}' for i in range(1, 4))
    return (f'<path d="M{x - 5} {y - 30} H{x + 5} V{y - 12} L{x + 4} {y + 7} {zuby} L{x - 4} {y + 7} L{x - 5} {y - 12} Z" fill="#9AA3AE" stroke="#5B6577" stroke-width="1"/>'
            f'<circle cx="{x}" cy="{y - 20}" r="2" fill="#5B6577"/>')


def treti_ruka():
    """Stojánek s ramenem a krokosvorkou, která drží kabel."""
    return ('<rect x="4" y="192" width="78" height="12" rx="4" fill="#5B6577"/><rect x="14" y="58" width="6" height="136" fill="#8A939F"/>'
            '<path d="M17 58 L60 48 L84 100" fill="none" stroke="#5B6577" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
            + ''.join(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="#1B2B4B"/>' for cx, cy in ((17, 58), (60, 48)))
            + krokosvorka(84) + '<text class="hint" x="68" y="46">třetí ruka</text>')


NAKRESY.update({
 'hlavolam': svg(21, hlavolam,
    'Hotový hlavolam: dráha je zastrčená v prkénku, na koncích izolepa. Baterie, vypínač, bzučák a očko jsou spojené lanky.',
    '-16 0 356 208'),
 'pajeni-postup': svg(22,
    # drát upnutý vlevo, páječka zprava shora, cín zleva zdola
    kabel('M30 130 H122', '#2F6FE0', 9) + med('M120 130 H196', 4) + treti_ruka()
    + '<g transform="translate(173 128) rotate(-36)">'
    + '<path d="M0 0 L28 -4 L28 4 Z" fill="#8A939F"/><rect x="28" y="-3" width="62" height="6" fill="#B9C1CB"/>'
    + '<rect x="86" y="-6" width="10" height="12" rx="2" fill="#5B6577"/><rect x="96" y="-9" width="84" height="18" rx="8" fill="#1B2B4B"/></g>'
    + f'<path d="M166 135 C162 158 158 182 155 206" fill="none" stroke="{CIN}" stroke-width="3" stroke-linecap="round"/>'
    + f'<ellipse cx="169" cy="131" rx="7" ry="4" fill="{CIN}"/><ellipse cx="167" cy="130" rx="2" ry="1" fill="#fff"/>'
    + note(188, 118, 230, 138, 'hrot ohřívá drát') + note(162, 162, 192, 176, 'cín přikládej k drátu,', odstup=5)
    + '<text class="lbl" x="196" y="194">ne na hrot</text>',
    'Hrot ohřívá drát shora, cín se přikládá z druhé strany k drátu a roztaví se jeho teplem.', '0 20 340 186'),
})

def pruzinka(x, y):
    """Pružinka v držáku baterií, 10 px na šířku, střed výšky v y."""
    body = ' '.join(f'{x + i * 2},{y + (-8 if i % 2 else 8)}' for i in range(6))
    return f'<polyline points="{body}" fill="none" stroke="#9AA6B8" stroke-width="2" stroke-linejoin="round"/>'
def clanek(x, y, plus_vpravo=True):
    """Tužková baterie 84 × 30 px: plochý mínus, plus s hrbolkem, znaménka na obalu."""
    hx = x + 84 if plus_vpravo else x - 4
    plus_x, minus_x = (x + 74, x + 10) if plus_vpravo else (x + 10, x + 74)
    tx = x + 38 if plus_vpravo else x + 46
    return (f'<rect x="{hx}" y="{y + 10}" width="4" height="10" rx="1" fill="#9AA6B8"/>'
            f'<rect x="{x}" y="{y}" width="84" height="30" rx="4" fill="#E9B425"/>'
            # hnědý konec u plusu jako u běžných baterií
            + (f'<rect x="{x + 62}" y="{y}" width="22" height="30" rx="4" fill="#9A5527"/><rect x="{x + 62}" y="{y}" width="6" height="30" fill="#9A5527"/>' if plus_vpravo
               else f'<rect x="{x}" y="{y}" width="22" height="30" rx="4" fill="#9A5527"/><rect x="{x + 16}" y="{y}" width="6" height="30" fill="#9A5527"/>')
            + 
            f'<text x="{tx}" y="{y + 13}" text-anchor="middle" font-size="10" font-weight="700" fill="#1B2B4B">AA</text>'
            f'<text x="{tx}" y="{y + 25}" text-anchor="middle" font-size="10" font-weight="700" fill="#1B2B4B">1,5 V</text>'
            f'<text x="{plus_x}" y="{y + 21}" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">+</text>'
            f'<text x="{minus_x}" y="{y + 21}" text-anchor="middle" font-size="14" font-weight="700" fill="#1B2B4B">−</text>')

def zkrut(x, y, w=26, holy=4):
    """Dva zkroucené drátky, konce v izolaci. holy je kus holého drátu mezi izolací a zkrutem."""
    a = f'M{x - w} {y} ' + ' '.join(f'Q{x - w + 6.5 + 13 * i} {y + (-5 if i % 2 else 5)} {x - w + 13 * (i + 1)} {y}' for i in range(4))
    b = f'M{x - w} {y} ' + ' '.join(f'Q{x - w + 6.5 + 13 * i} {y + (5 if i % 2 else -5)} {x - w + 13 * (i + 1)} {y}' for i in range(4))
    return (kabel(f'M{x - w - holy - 16} {y} H{x - w - holy}', '#2F6FE0', 9) + kabel(f'M{x + w + holy} {y} H{x + w + holy + 16}', '#2F6FE0', 9)
            + med(f'M{x - w - holy - 2} {y} H{x - w}', 3) + med(f'M{x + w} {y} H{x + w + holy + 2}', 3) + med(a, 3) + med(b, 3))

def popisek(x, y, *radky, znak='', barva='#1B2B4B'):
    t = f'<text class="lbl" x="{x}" y="{y}" text-anchor="middle" style="fill:{barva};font-size:14px">{znak}</text>' if znak else ''
    return t + ''.join(f'<text class="lbl" x="{x}" y="{y + 18 + 14 * i}" text-anchor="middle">{r}</text>' for i, r in enumerate(radky))

hrbolky = ' '.join(f'{170 + (12 + (2.5 if i % 2 else 0)) * math.cos(i * math.pi / 7):.1f},{78 + (11 + (2.5 if i % 2 else 0)) * math.sin(i * math.pi / 7):.1f}' for i in range(14))
# Držák 2× AA shora: dva články vedle sebe, vývody vpravo (+ nahoře v y 77, − dole v y 123)
drzak_2aa = (
    '<rect x="24" y="56" width="128" height="88" rx="6" fill="#3B4A63"/>'
    # články v sérii, každý otočený obráceně: plochý mínus vždy k pružince
    + ''.join(f'<polyline points="{b}" fill="none" stroke="#9AA6B8" stroke-width="3" stroke-linejoin="round"/>'
              for b in ('35,79 31,79 31,121 39,121', '133,79 144,79 144,77 152,77', '137,121 144,121 144,123 152,123'))
    + clanek(46, 64, plus_vpravo=True) + pruzinka(34, 79) + clanek(42, 106, plus_vpravo=False) + pruzinka(128, 121)
    + '<rect x="152" y="74" width="10" height="6" fill="#9AA6B8"/><rect x="152" y="120" width="10" height="6" fill="#9AA6B8"/>'
    + '<text class="lbl" x="166" y="72" style="font-size:15px">+</text><text class="lbl" x="166" y="140" style="font-size:15px">−</text>'
)

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
    + kabel('M262 85 C282 85 292 110 304 128', MODRA, 4) + spoj(262, 85, 4)
    + dim_v(62, 57, 113, '1,5–2 cm')
    + note(117, 103, 140, 126, 'mezera, aby šlo očko')
    + '<text class="lbl" x="144" y="144">nasadit na dráhu</text>'
    + note(200, 79, 200, 52, 'rukojeť omotaná izolepou', 'middle') + note(278, 91, 300, 52, 'lanko', 'middle', odstup=5),
    'Očko ohnuté kolem fixy, s mezerou. Rukojeť je omotaná izolepou, na konci je připájené lanko.', '0 30 340 124'),
 'zapojeni': svg(25,
    drzak_2aa
    # bzučák z boku: delší nožka je plus
    + '<rect x="236" y="20" width="40" height="26" rx="4" fill="#1B2B4B"/><text x="246" y="38" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">+</text>'
    + '<line x1="246" y1="46" x2="246" y2="86" stroke="#9AA6B8" stroke-width="2.5"/><line x1="266" y1="46" x2="266" y2="72" stroke="#9AA6B8" stroke-width="2.5"/>'
    + vypinac_bok(182, 58, 36, 18, 14)
    + kabel('M162 77 C178 77 186 90 191 90', '#E0402B', 3.5) + spoj(162, 77) + spoj(191, 90)
    + kabel('M209 90 C224 90 234 86 246 86', '#E0402B', 3.5) + spoj(209, 90) + spoj(246, 86)
    + kabel('M266 72 C280 72 290 84 300 84', '#E0402B', 3.5) + spoj(266, 72)
    + '<line x1="300" y1="84" x2="324" y2="84" stroke="#1B2B4B" stroke-width="2" marker-end="url(#sip{n})"/>'
    + '<text class="lbl" x="322" y="104" text-anchor="end">k dráze</text>'
    + kabel('M162 123 C200 123 240 150 300 150', MODRA, 3.5) + spoj(162, 123)
    + '<line x1="300" y1="150" x2="324" y2="150" stroke="#1B2B4B" stroke-width="2" marker-end="url(#sip{n})"/>'
    + '<text class="lbl" x="322" y="170" text-anchor="end">k očku</text>'
    + note(276, 33, 292, 33, 'bzučák') + note(246, 91, 240, 104, 'delší nožka +', 'end')
    + note(200, 50, 200, 40, 'vypínač', 'middle'),
    'Zapojení: plus baterie přes vypínač k delší nožce bzučáku, druhá nožka k dráze, mínus baterie dlouhým lankem k očku. Baterie jsou v držáku každá obráceně, plochým mínusem k pružince. Tečky jsou pájené spoje.',
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
    vodic('30,58 30,30 200,30') + '<circle cx="55" cy="30" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/><circle cx="85" cy="30" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/>' + vodic('200,30 305,30')
    + vodic('115,30 115,70 145,70') + vodic('170,70 200,70 200,30')
    + vodic('225,30 225,75') + vodic('225,105 225,150') + vodic('305,30 305,78') + vodic('305,108 305,150 30,150 30,111')
    # očko a dráha jako spínač v barvě mědi; přes ně je vodič přerušený
    + '<line x1="140" y1="30" x2="175" y2="30" stroke="#EDF1F4" stroke-width="5"/><rect x="140" y="26" width="35" height="8" fill="#fff"/>'
    + sp(145, 170, 30, MED) + sp(145, 170, 70)
    # baterie: kryt na 2× AA a za ním do série kryt na 1× AA, dohromady 4,5 V
    + '<rect x="12" y="50" width="36" height="39" rx="5" fill="none" stroke="#9AA6B8" stroke-width="1.2" stroke-dasharray="3 3"/>'
    + '<rect x="12" y="97" width="36" height="21" rx="5" fill="none" stroke="#9AA6B8" stroke-width="1.2" stroke-dasharray="3 3"/>'
    + '<g stroke="#1B2B4B" stroke-linecap="round">'
    + ''.join(f'<line x1="18" y1="{y}" x2="42" y2="{y}" stroke-width="2.5"/><line x1="24" y1="{y + 7}" x2="36" y2="{y + 7}" stroke-width="4"/>'
              for y in (58, 75, 104)) + '</g>'
    + vodic('30,65 30,75') + vodic('30,82 30,104')
    + '<text class="lbl" x="52" y="60">+</text>'
    + '<text class="lbl" x="7" y="74" text-anchor="end">2× AA</text><text class="lbl" x="7" y="112" text-anchor="end">1× AA</text>'
    + '<text class="hint" x="7" y="136" text-anchor="end">= 4,5 V</text>'
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
    'Schéma v klidu, vypínač je zapnutý. Napájí ho kryt na 2× AA a za ním kryt na 1× AA, dohromady 4,5 V. Kontakt relé je zapojený vedle očka a dráhy: když ho cívka přitáhne, vede proud místo nich.',
    '-40 0 380 162')

TMAVA = '#1B2B4B'
pramenky = ''.join(med(f'M180 80 Q192 80 204 {80 + d}', 1.4) for d in (-7, -3.5, 0, 3.5, 7))
NAKRESY['odizolovani'] = svg(27,
    kabel('M11 80 H97', '#2F6FE0', 9) + '<line x1="81" y1="70" x2="81" y2="90" stroke="#1B2B4B" stroke-width="1.5" stroke-dasharray="3 2"/>'
    + dim_h(81, 101, 64, '1 cm') + popisek(57, 112, 'kleštěmi asi', '1 cm od konce', znak='1. naříznout', barva=TMAVA)
    + kabel('M124 80 H176', '#2F6FE0', 9) + pramenky + kabel('M212 80 H222', '#2F6FE0', 9)
    + popisek(170, 112, 'izolace sjede,', 'drátky trčí', znak='2. stáhnout', barva=TMAVA)
    + kabel('M237 80 H289', '#2F6FE0', 9) + med('M289 80 H317', 4)
    + ''.join(f'<line x1="{x}" y1="78" x2="{x + 3}" y2="82" stroke="{MED_TMAVA}" stroke-width="1"/>' for x in range(292, 315, 4))
    + popisek(283, 112, 'prsty do sebe,', 'ať neodstávají', znak='3. zakroutit', barva=TMAVA),
    'Odizolování lanka: naříznout izolaci asi 1 cm od konce, stáhnout ji a tenké drátky zakroutit do sebe.', '0 50 340 102')
NAKRESY['spojeni'] = svg(28,
    zkrut(85, 80, holy=12) + popisek(85, 112, 'konce zakruťte', 'do sebe', znak='zakroucené', barva=TMAVA)
    # háčky provlečené jako dva články řetězu: nahoře je přes pravý levý, dole pravý přes levý
    + kabel('M200 89 H226', '#2F6FE0', 9) + med('M224 89 H248 A9 9 0 1 0 239 80', 3)
    + kabel('M284 71 H310', '#2F6FE0', 9) + med('M286 71 H262 A9 9 0 1 0 271 80', 3).replace(MED, MED_TMAVA)
    + '<path d="M256.16 76.2 A9 9 0 0 0 253.16 72.63" fill="none" style="stroke:var(--paper)" stroke-width="7"/>'
    + med('M256.16 76.2 A9 9 0 0 0 253.16 72.63', 3)
    + popisek(255, 112, 'zahákněte', 'jeden za druhý', znak='dva háčky', barva=TMAVA),
    'Dva způsoby, jak drátky spojit před pájením: zakroutit do sebe, nebo zaháknout jako dva háčky.', '0 50 340 102')


# --- ikony nářadí pro kartičky „Co budeme používat“, viewBox 120 × 80 ---

SEDA, SEDA_SVETLA, SEDA_TMAVA, MOSAZ = '#8A939F', '#B9C1CB', '#5B6577', '#C9A23A'
cara = 'fill="none" stroke-linecap="round" stroke-linejoin="round"'


def kleste(cerist, rukojeti):
    """Kleště ležící čelistmi doleva, kloub v (52, 40)."""
    return (f'<path d="M52 38 C70 30 90 24 112 24" {cara} stroke="{rukojeti}" stroke-width="8"/>'
            f'<path d="M52 42 C70 50 90 56 112 56" {cara} stroke="{rukojeti}" stroke-width="8"/>'
            + cerist + f'<circle cx="52" cy="40" r="4.5" fill="{SEDA_TMAVA}"/>')


IKONY = {
    'pajecka': f'<rect x="8" y="64" width="56" height="10" rx="3" fill="{SEDA_TMAVA}"/><rect x="28" y="54" width="4" height="12" fill="{SEDA}"/>'
        '<path d="M20 60 L30 55 L30 51 Z" fill="#8A939F"/><path d="M29 52 L62 34" stroke="#B9C1CB" stroke-width="4"/>'
        '<rect x="60" y="28" width="8" height="9" rx="2" fill="#5B6577" transform="rotate(-30 64 32)"/>'
        '<path d="M70 28 L106 8" stroke="#1B2B4B" stroke-width="12" stroke-linecap="round"/>'
        + ''.join(f'<ellipse cx="{30 + 6 * i}" cy="{56 - 3.4 * i}" rx="4" ry="9" fill="none" stroke="{SEDA}" stroke-width="1.6" transform="rotate(-30 {30 + 6 * i} {56 - 3.4 * i})"/>' for i in range(5)),
    'cin': f'<path d="M62 60 C80 70 98 62 112 46" {cara} stroke="{CIN}" stroke-width="3"/>'
        f'<circle cx="44" cy="40" r="27" fill="#DDE2E8" stroke="{SEDA}" stroke-width="2"/><circle cx="44" cy="40" r="20" fill="{CIN}"/>'
        + ''.join(f'<circle cx="44" cy="40" r="{r}" fill="none" stroke="#9AA3AE" stroke-width="0.8"/>' for r in (12, 15, 18))
        + f'<circle cx="44" cy="40" r="8" fill="#fff" stroke="{SEDA}" stroke-width="2"/>',
    'dratenka': ''.join(f'<circle cx="{34 + 4.2 * i}" cy="{44 + (-6 if i % 2 else 2)}" r="8" fill="none" stroke="{MOSAZ}" stroke-width="1.6"/>' for i in range(13))
        + f'<path d="M20 48 L28 68 H92 L100 48 Z" fill="{SEDA_TMAVA}"/><ellipse cx="60" cy="48" rx="40" ry="5" fill="none" stroke="{SEDA}" stroke-width="2"/>',
    'treti-ruka': f'<rect x="8" y="66" width="50" height="9" rx="3" fill="{SEDA_TMAVA}"/><rect x="17" y="18" width="5" height="50" fill="{SEDA}"/>'
        f'<path d="M20 20 L56 12 L80 22" {cara} stroke="{SEDA_TMAVA}" stroke-width="3"/>'
        + ''.join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#1B2B4B"/>' for x, y in ((20, 20), (56, 12)))
        + kabel('M64 52 H94', '#2F6FE0', 8) + med('M94 52 H112', 3) + krokosvorka(80, 52),
    'podlozka': '<rect x="8" y="14" width="104" height="54" rx="7" fill="#2E8C82"/>'
        + ''.join(f'<circle cx="{x}" cy="30" r="7" fill="#4FB0A5"/>' for x in (26, 46, 66))
        + '<rect x="80" y="22" width="22" height="16" rx="3" fill="#4FB0A5"/><rect x="20" y="46" width="82" height="12" rx="3" fill="#4FB0A5"/>',
    'odizolovaci-kleste': kleste(
        f'<path d="M54 35 L10 37 L10 40 L54 40 Z" fill="{SEDA}"/><path d="M54 40 L10 40 L10 43 L54 45 Z" fill="{SEDA_TMAVA}"/>'
        + ''.join(f'<circle cx="{x}" cy="40" r="{r}" fill="#fff" stroke="#1B2B4B" stroke-width="1"/>' for x, r in ((22, 1.8), (31, 2.3), (41, 2.8))),
        '#E0402B'),
    'stipacky': kleste(
        f'<path d="M54 32 L24 36 L14 40 L54 40 Z" fill="{SEDA}"/><path d="M54 40 L14 40 L24 44 L54 48 Z" fill="{SEDA_TMAVA}"/>',
        '#E9B425'),
    'drat-lanko': kabel('M10 24 H62', '#2F6FE0', 9) + med('M62 24 H82', 4)
        + kabel('M10 56 H62', '#2F6FE0', 9) + ''.join(med(f'M62 56 Q72 56 82 {56 + d}', 1.3) for d in (-6, -3, 0, 3, 6))
        + '<text class="ikona-popisek" x="88" y="28">drát</text><text class="ikona-popisek" x="88" y="60">lanko</text>',
    'izolepa': '<path d="M44 62 H106 L102 65 L106 68 H44 Z" fill="#1B2B4B"/>'
        '<circle cx="44" cy="40" r="27" fill="#1B2B4B"/><circle cx="44" cy="40" r="14" style="fill:var(--paper)" stroke="#C8CDD3" stroke-width="4"/>',
    'bryle': '<path d="M14 38 H4 M106 38 H116" stroke="#1B2B4B" stroke-width="4" stroke-linecap="round"/>'
        + ''.join(f'<rect x="{x}" y="22" width="44" height="32" rx="13" fill="#D6ECF5" stroke="#1B2B4B" stroke-width="3.5"/>'
                  f'<path d="M{x + 9} 30 L{x + 17} 30" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x in (12, 64))
        + '<path d="M56 34 Q60 29 64 34" fill="none" stroke="#1B2B4B" stroke-width="3.5"/>',
}


def ikona(jmeno):
    return f'<svg class="ikona" viewBox="0 0 120 80" aria-hidden="true">{IKONY[jmeno]}</svg>'


# --- vibrobot z kartáče ---
DREVO = 'fill="#C9955A" stroke="#8C6234" stroke-width="1.5"'
STETINA = '#4A3B2A'
POCINOVANE = 'fill="#C3CAD3" stroke="#7D8794" stroke-width="1.2"'
EXCENTR = '#13A39A'


def motor_bok(x, y, w=44, h=28):
    """Motorek z boku: zadní víčko s vývody vlevo v x, plechové tělo, vpravo ložisko a hřídel."""
    return (f'<rect x="{x - 5}" y="{y + 6}" width="5" height="3" fill="#9AA6B8"/>'
            f'<rect x="{x - 5}" y="{y + h - 9}" width="5" height="3" fill="#9AA6B8"/>'
            f'<rect x="{x}" y="{y + 4}" width="8" height="{h - 8}" rx="2" fill="#5B6577"/>'
            f'<rect x="{x + 6}" y="{y}" width="{w}" height="{h}" rx="6" {POCINOVANE}/>'
            f'<rect x="{x + 6 + w}" y="{y + h / 2 - 5}" width="4" height="10" fill="#7D8794"/>')


vibrobot = (
    '<line class="ground" x1="20" y1="179" x2="320" y2="179"/>'
    # štětiny skloněné konci dozadu (doprava), robot jede dopředu (doleva)
    + ''.join(f'<line x1="{x}" y1="150" x2="{x + 9}" y2="178" stroke="{STETINA}" stroke-width="2" stroke-linecap="round"/>'
              for x in range(48, 284, 6))
    + f'<rect x="40" y="128" width="250" height="22" rx="6" {DREVO}/>'
    # druhý drát od mínusu vede za vypínačem
    + kabel('M150 118 C170 134 184 110 195 104', MODRA, 3)
    + '<rect x="56" y="106" width="96" height="22" rx="3" fill="#3B4A63"/>'
    + '<text x="104" y="121" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">2× AA</text>'
    + '<rect x="132" y="103" width="7" height="28" rx="2" fill="none" stroke="#E8487A" stroke-width="2"/>'
    + vypinac_bok(164, 114)
    + kabel('M148 108 C152 96 160 100 166 112', '#E0402B', 3)
    + kabel('M184 112 C188 100 190 92 195 92', '#E0402B', 3)
    # podložka a motorek, excentr se šroubkem končí před okrajem kartáče
    + '<rect x="204" y="112" width="48" height="16" rx="2" fill="#D9B98C" stroke="#9C7442" stroke-width="1.2"/>'
    + motor_bok(200, 84)
    + '<line x1="254" y1="98" x2="266" y2="98" stroke="#7D8794" stroke-width="2.5"/>'
    + f'<rect x="262" y="93" width="8" height="10" rx="1" fill="{EXCENTR}"/><rect x="263" y="72" width="6" height="29" rx="3" fill="{EXCENTR}"/>'
    + '<rect x="258" y="75" width="22" height="5" fill="#9AA3AE"/><rect x="279" y="72" width="4" height="11" rx="1" fill="#7D8794"/>'
    # oko a tykadlo z chlupatého drátku
    + '<path d="M60 106 C54 88 38 86 34 72 C32 64 42 62 42 70" fill="none" stroke="#E8487A" stroke-width="3.5" stroke-linecap="round"/>'
    + '<circle cx="50" cy="120" r="8" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/><circle cx="47" cy="122" r="3.5" fill="#1B2B4B"/>'
    + '<line x1="110" y1="50" x2="44" y2="50" stroke="#1B2B4B" stroke-width="2" marker-end="url(#sip{n})"/>'
    + '<text class="lbl" x="116" y="54">jede tam</text>'
    + note(174, 108, 150, 88, 'vypínač', 'end') + note(226, 84, 214, 64, 'motorek', 'end')
    + note(281, 72, 300, 56, 'excentr') + '<text class="lbl" x="304" y="74">se šroubkem</text>'
    + note(252, 122, 300, 140, 'podložka')
    + '<text class="lbl" x="150" y="193" text-anchor="middle">štětiny skloněné dozadu</text>'
)

# Excentr zepředu, měřítko 3 px na 1 mm: motor 20 × 15 mm, šroubek 6 mm od osy, opisuje kružnici asi 9,5 mm.
OSA_X, OSA_Y = 130, 110
sroub_x, sroub_y = OSA_X + 12.7, OSA_Y - 12.7
excentr_zepredu = (
    '<line class="ground" x1="20" y1="195" x2="240" y2="195"/>'
    + ''.join(f'<line x1="{x}" y1="172" x2="{x}" y2="194" stroke="{STETINA}" stroke-width="2" stroke-linecap="round"/>'
              for x in range(46, 218, 6))
    + f'<rect x="40" y="150" width="180" height="22" rx="5" {DREVO}/><text class="hint" x="50" y="165">kartáč</text>'
    + '<rect x="100" y="132" width="60" height="18" rx="2" fill="#D9B98C" stroke="#9C7442" stroke-width="1.2"/>'
    + f'<path d="M108 87 H152 A30 30 0 0 1 152 132 H108 A30 30 0 0 1 108 87 Z" {POCINOVANE}/>'
    + f'<circle cx="{OSA_X}" cy="{OSA_Y}" r="28.5" fill="none" stroke="{EXCENTR}" stroke-width="1.8" stroke-dasharray="5 4"/>'
    + f'<line x1="{OSA_X}" y1="{OSA_Y}" x2="{sroub_x}" y2="{sroub_y}" stroke="{EXCENTR}" stroke-width="21" stroke-linecap="round"/>'
    + f'<circle cx="{sroub_x}" cy="{sroub_y}" r="8" fill="#9AA3AE" stroke="#5B6577" stroke-width="1.2"/>'
    + f'<path d="M{sroub_x - 4} {sroub_y} h8 M{sroub_x} {sroub_y - 4} v8" stroke="#5B6577" stroke-width="1.6"/>'
    + f'<circle cx="{OSA_X}" cy="{OSA_Y}" r="3" fill="#1B2B4B"/>'
    # osa musí být výš nad kartáčem, než kam dosáhne šroubek
    + f'<line x1="{OSA_X}" y1="{OSA_Y}" x2="204" y2="{OSA_Y}" stroke="#4A5875" stroke-width="1" stroke-dasharray="3 3"/>'
    + f'<g class="dim"><line x1="200" y1="{OSA_Y}" x2="200" y2="150"/><line x1="195" y1="{OSA_Y}" x2="205" y2="{OSA_Y}"/><line x1="195" y1="150" x2="205" y2="150"/></g>'
    + '<text class="lbl" x="210" y="127">osa aspoň</text><text class="lbl" x="210" y="141">11 mm nad kartáčem</text>'
    + note(sroub_x, sroub_y, 178, 64, 'šroubek M3 je závaží', odstup=13)
    + note(108, 92, 80, 64, 'kudy jede šroubek', 'middle')
    + note(160, 144, 238, 172, 'podložka')
)

NAKRESY.update({
 'vibrobot': svg(31, vibrobot,
    'Hotový vibrobot z boku: na kartáči je držák baterií, vypínač a na podložce motorek. Excentr se šroubkem se točí nad kartáčem a nepřečnívá přes jeho okraj.',
    '0 30 360 172'),
 'vibrobot-excentr': svg(32, excentr_zepredu,
    'Pohled zepředu na hřídel: šroubek v excentru opisuje kružnici. Podložka zvedne motorek tak, aby šroubek nikdy neškrtl o kartáč.',
    '0 50 340 152'),
 'vibrobot-zapojeni': svg(33,
    drzak_2aa + vypinac_bok(182, 58, 36, 18, 14)
    + motor_bok(244, 58, 60, 44)
    + '<line x1="314" y1="80" x2="330" y2="80" stroke="#7D8794" stroke-width="2.5"/>'
    + kabel('M162 77 C178 77 186 90 191 90', '#E0402B', 3.5) + spoj(162, 77) + spoj(191, 90)
    + kabel('M209 90 C224 90 228 65 239 65', '#E0402B', 3.5) + spoj(209, 90) + spoj(239, 65)
    + kabel('M162 123 C200 123 222 95 239 95', MODRA, 3.5) + spoj(162, 123) + spoj(239, 95)
    + note(200, 50, 200, 40, 'vypínač', 'middle') + note(282, 58, 282, 40, 'motorek', 'middle')
    + '<text class="hint" x="282" y="124" text-anchor="middle">vývody motorku</text>'
    + '<text class="hint" x="282" y="137" text-anchor="middle">lze prohodit</text>',
    'Zapojení: plus baterie přes vypínač k jednomu vývodu motorku, mínus baterie k druhému. Tečky jsou pájené spoje.',
    '0 8 340 172'),
})


# --- hlavolam: LED s odporem vedle bzučáku (rozšíření), bzučák nožkami dolů ---
def odpor_svisle(x, y1, y2, pruhy=('#8B4A1C', '#1B1B1B', '#8B4A1C')):
    """Odpor nastojato, tělo mezi y1 a y2, barevné proužky odshora; poslední zlatý."""
    p = ''.join(f'<rect x="{x - 6}" y="{y1 + 5 + 6 * i}" width="12" height="3" fill="{b}"/>' for i, b in enumerate(pruhy))
    return (f'<rect x="{x - 6}" y="{y1}" width="12" height="{y2 - y1}" rx="5" fill="#E8D3A8" stroke="#A88B5A" stroke-width="1"/>'
            + p + f'<rect x="{x - 6}" y="{y2 - 9}" width="12" height="3" fill="#C9A23A"/>')


NAKRESY['hlavolam-led'] = svg(34,
    '<rect x="115" y="20" width="40" height="26" rx="4" fill="#1B2B4B"/><text x="145" y="38" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">+</text>'
    + '<line x1="125" y1="46" x2="125" y2="80" stroke="#9AA6B8" stroke-width="2.5"/><line x1="145" y1="46" x2="145" y2="90" stroke="#9AA6B8" stroke-width="2.5"/>'
    # lanka, která už jsou zapájená z minula
    + kabel('M125 80 C100 80 80 70 44 70', '#E0402B', 3.5) + '<text class="lbl" x="44" y="62">k dráze</text>'
    + kabel('M145 90 C175 90 200 70 256 70', '#E0402B', 3.5) + '<text class="lbl" x="256" y="62" text-anchor="end">od vypínače</text>'
    # nové: odpor na plusovou nožku, LED hlavičkou dolů; plusová nožka LED je viditelně delší
    + '<path d="M145 90 V94 Q145 99 150 99 H167 Q172 99 172 104 V106 M172 134 V139 Q172 144 167 144 H145" fill="none" stroke="#9AA6B8" stroke-width="2"/>'
    + odpor_svisle(172, 106, 134)
    + '<line x1="145" y1="144" x2="145" y2="180" stroke="#9AA6B8" stroke-width="2.5"/>'
    + '<line x1="129" y1="158" x2="129" y2="180" stroke="#9AA6B8" stroke-width="2.5"/>'
    + kabel('M125 80 C125 110 129 130 129 158', '#1B2B4B', 3)
    # LED: okraj je na mínusové straně (vlevo) zkosený, plusová strana přečnívá
    + '<path d="M126 180 H152 V186 H126 Z" fill="#B8331F"/>'
    + '<path d="M126 186 V200 A11 11 0 0 0 148 200 V186 Z" fill="#E0402B"/><ellipse cx="132" cy="197" rx="2.5" ry="5" fill="#fff" fill-opacity=".5"/>'
    + '<line x1="152" y1="180" x2="152" y2="186" stroke="#8E2615" stroke-width="1"/>'
    + spoj(125, 80) + spoj(145, 90) + spoj(129, 158, 4) + spoj(145, 144, 4)
    + note(155, 30, 186, 30, 'bzučák')
    + note(178, 120, 200, 120, 'odpor 100 Ω')
    + note(145, 162, 186, 158, 'delší nožka: plus', odstup=4)
    + note(129, 170, 100, 160, 'kratší nožka', 'end', odstup=4) + '<text class="lbl" x="96" y="180" text-anchor="end">mínus</text>'
    + note(126, 183, 100, 200, 'zkosení: mínus', 'end')
    + note(150, 204, 186, 204, 'LED')
    # LED zblízka, před připájením: hlavičkou nahoru, delší nožka plus, zkosení na straně mínusu
    + '<rect x="334" y="22" width="126" height="196" rx="10" fill="none" stroke="#C9D2DE" stroke-dasharray="4 4"/>'
    + '<text class="lbl" x="397" y="42" text-anchor="middle">LED zblízka</text>'
    + '<path d="M384 112 V82 A17 17 0 0 1 418 82 V112 Z" fill="#E0402B"/><ellipse cx="392" cy="86" rx="3.5" ry="9" fill="#fff" fill-opacity=".5"/>'
    + '<path d="M384 112 H426 V120 H384 Z" fill="#B8331F"/>'
    + '<line x1="392" y1="120" x2="392" y2="160" stroke="#9AA6B8" stroke-width="3"/>'
    + '<line x1="410" y1="120" x2="410" y2="194" stroke="#9AA6B8" stroke-width="3"/>'
    + '<text x="392" y="180" text-anchor="middle" font-size="22" font-weight="700" fill="#1B2B4B">−</text>'
    + '<text x="410" y="213" text-anchor="middle" font-size="20" font-weight="700" fill="#E0402B">+</text>'
    + '<text class="lbl" x="386" y="148" text-anchor="end">kratší</text>'
    + '<text class="lbl" x="416" y="172">delší</text>'
    + note(384, 115, 366, 98, 'zkosení', 'end'),
    'LED s odporem vedle bzučáku: odpor na delší (plusovou) nožku bzučáku, na něj delší nožka LED. Kratší nožka LED, na jejíž straně má LED zkosený okraj, se připojí kouskem lanka na kratší nožku bzučáku. Tečky jsou pájené spoje.',
    '0 8 470 214')


# --- hotový hlavolam s pamětí: relé na nožkách bzučáku, napájení 2× AA + 1× AA ---
draha_rele = ('M60 170 V128 C60 98 90 88 108 102 C126 116 124 134 146 132 C170 130 170 92 196 92 '
              'C222 92 220 124 244 120 C270 116 272 92 300 92 C326 92 322 126 346 120 C372 114 380 110 380 128 V170')
RELE = '#2F5FC0'
hlavolam_rele = (
    f'<rect x="30" y="170" width="380" height="16" rx="3" {KAR}/>'
    + '<text class="hint" x="402" y="181" text-anchor="end">prkénko</text>'
    # baterie: kryt na 1× AA a kryt na 2× AA za sebou, krátké lanko spojí mínus dvojky s plusem jedničky
    + '<rect x="72" y="152" width="34" height="18" rx="3" fill="#3B4A63"/><rect x="106" y="157" width="3" height="8" fill="#3B4A63"/>'
    + '<text x="89" y="165" text-anchor="middle" font-size="9" font-weight="700" fill="#fff">1× AA</text>'
    + '<rect x="122" y="150" width="56" height="20" rx="3" fill="#3B4A63"/><rect x="178" y="155" width="4" height="10" fill="#3B4A63"/>'
    + '<text x="150" y="164" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">2× AA</text>'
    + kabel('M109 161 C114 161 116 160 122 160', MODRA, 3)
    + vypinac_bok(194, 156)
    + '<rect x="232" y="152" width="22" height="18" rx="3" fill="#1B2B4B"/><text x="238" y="165" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">+</text>'
    # relé s diodou navrchu, proužek diody k plusu (k bzučáku)
    + f'<rect x="282" y="144" width="38" height="26" rx="3" fill="{RELE}"/>'
    + '<text x="301" y="161" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">relé</text>'
    + '<line x1="289" y1="144" x2="289" y2="139" stroke="#9AA6B8" stroke-width="1.5"/><line x1="313" y1="144" x2="313" y2="139" stroke="#9AA6B8" stroke-width="1.5"/>'
    + '<rect x="292" y="135" width="18" height="7" rx="2" fill="#1B1B1B"/><rect x="294" y="135" width="3" height="7" fill="#C9D2DE"/>'
    + '<line x1="289" y1="139" x2="292" y2="139" stroke="#9AA6B8" stroke-width="1.5"/><line x1="310" y1="139" x2="313" y2="139" stroke="#9AA6B8" stroke-width="1.5"/>'
    + med(draha_rele) + izolepa(55, 128, 10, 28) + izolepa(375, 128, 10, 28)
    # plus: držák → vypínač → bzučák; bzučák → cívka relé; relé (COM) → dráha
    + kabel('M182 160 C188 160 190 164 194 164', '#E0402B', 3)
    + kabel('M216 164 C222 164 226 166 232 166', '#E0402B', 3)
    + kabel('M254 158 C266 158 270 154 282 154', '#E0402B', 3)
    + kabel('M254 166 C266 166 270 164 282 164', '#E0402B', 3)
    + kabel('M320 164 C344 164 360 165 376 165', '#E0402B', 3) + spoj(379, 165, 3.5)
    # mínus: kontakt relé (NO) po prkénku k mínusu baterie, odtud dlouhé lanko k očku
    + kabel('M320 168 C330 174 324 177 310 177 H82 C74 177 70 173 72 166', MODRA, 3)
    + f'<ellipse cx="196" cy="92" rx="5" ry="13" fill="none" stroke="{MED_TMAVA}" stroke-width="3"/>'
    + med('M196 80 L200 30', 3) + izolepa(195, 30, 10, 34)
    + kabel('M200 30 C204 6 120 4 60 40 C20 64 30 150 72 160', MODRA, 3)
    + note(55, 140, 14, 120, 'start', 'end') + note(385, 140, 412, 120, 'cíl', 'end')
    + note(119, 108, 124, 62, 'dráha', 'middle', odstup=5) + note(205, 46, 240, 34, 'očko s rukojetí')
    + note(243, 151, 252, 128, 'bzučák', 'middle')
    + note(301, 134, 330, 112, 'dioda')
    + note(205, 170, 205, 200, 'vypínač', 'middle')
    + note(262, 180, 250, 198, 'lanko od relé k mínusu')
)
NAKRESY['hlavolam-rele-sestava'] = svg(35, hlavolam_rele,
    'Hotový hlavolam s pamětí. Za kryt na 2× AA je zapojený kryt na 1× AA, dohromady 4,5 V. Relé má cívku připojenou na obě nožky bzučáku, dioda je přes cívku proužkem k plusu. Kontakt relé vede od dráhy po prkénku k mínusu baterie, tedy vedle očka.',
    '-16 0 436 216')


# --- svítící ozdoba: LED na knoflíkové baterii, LED k boxu CR2032, hotová ozdoba ---
CERVENA = '#E0402B'
ORANZOVA = '#F08A24'
NOZKA = 'stroke="#9AA6B8" stroke-width="3" stroke-linecap="round"'
def paprsky(cx, cy, r1, r2, uhly):
    """Krátké žluté paprsky kolem svítící LED."""
    return ''.join(f'<line x1="{cx + r1 * math.cos(math.radians(u)):.1f}" y1="{cy + r1 * math.sin(math.radians(u)):.1f}" '
                   f'x2="{cx + r2 * math.cos(math.radians(u)):.1f}" y2="{cy + r2 * math.sin(math.radians(u)):.1f}" '
                   'stroke="#E9B425" stroke-width="3" stroke-linecap="round"/>' for u in uhly)
def hvezda(cx, cy, R, r):
    body = ' '.join(f'{cx + (R if i % 2 == 0 else r) * math.sin(i * math.pi / 5):.1f},{cy - (R if i % 2 == 0 else r) * math.cos(i * math.pi / 5):.1f}'
                    for i in range(10))
    return f'<polygon points="{body}" {KAR} stroke-linejoin="round"/>'

NAKRESY['led-knoflik'] = svg(36,
    # LED hlavičkou nahoru, zkosení vlevo (mínus), plusová strana okraje přečnívá vpravo
    paprsky(168, 62, 24, 34, (-160, -125, -90, -55, -20))
    + '<path d="M151 92 V62 A17 17 0 0 1 185 62 V92 Z" fill="#E0402B"/><ellipse cx="159" cy="66" rx="3.5" ry="9" fill="#fff" fill-opacity=".5"/>'
    + '<path d="M151 92 H193 V100 H151 Z" fill="#B8331F"/>'
    + f'<line x1="158" y1="100" x2="158" y2="166" {NOZKA}/><line x1="178" y1="100" x2="178" y2="202" {NOZKA}/>'
    # knoflíková baterie z boku: vpravo rovná strana plus, vlevo menší vystouplý mínus
    + f'<rect x="160" y="128" width="3.5" height="54" fill="#A9B2BE" stroke="#7D8794" stroke-width="1"/>'
    + f'<rect x="163.5" y="120" width="13" height="70" rx="2" fill="#C3CAD3" stroke="#7D8794" stroke-width="1"/>'
    + '<text x="195" y="133" font-size="16" font-weight="700" fill="#E0402B">+</text>'
    + '<text x="143" y="186" font-size="18" font-weight="700" fill="#1B2B4B">−</text>'
    + note(180, 196, 214, 196, 'delší nožka: plus')
    + '<text class="hint" x="218" y="212">ke straně s nápisem</text>'
    + note(156, 158, 128, 150, 'kratší nožka: mínus', 'end')
    + note(150, 70, 126, 58, 'LED', 'end')
    + note(176, 126, 214, 112, 'knoflíková baterie')
    + '<text class="hint" x="218" y="128">z boku</text>',
    'LED na knoflíkové baterii: delší nožka (plus) se přiloží na stranu baterie s nápisem a značkou +, kratší nožka na druhou stranu. Obráceně LED nesvítí.',
    '0 20 340 200')

NAKRESY['ozdoba-zapojeni'] = svg(37,
    # box CR2032 shora s posuvným vypínačem na horní hraně
    '<rect x="20" y="62" width="92" height="76" rx="8" fill="#23272E"/>'
    + '<circle cx="66" cy="100" r="25" fill="none" stroke="#4A515C" stroke-width="2"/>'
    + '<text x="66" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">CR2032</text>'
    + '<rect x="54" y="54" width="22" height="9" rx="2" fill="#4A515C"/><rect x="58" y="51" width="8" height="6" rx="1" fill="#9AA6B8"/>'
    # vodiče z boxu k nožkám LED
    + kabel('M112 80 C160 80 180 90 220 90', CERVENA, 3.5) + kabel('M112 120 C170 120 210 110 260 110', CERNA, 3.5)
    # LED naležato, hlavičkou doprava: zkosení dole (mínus), plusová strana okraje přečnívá nahoru
    + f'<line x1="226" y1="90" x2="300" y2="90" {NOZKA}/><line x1="266" y1="110" x2="300" y2="110" {NOZKA}/>'
    + '<path d="M300 75 H308 V117 H300 Z" fill="#B8331F"/>'
    + '<path d="M308 83 H322 A17 17 0 0 1 322 117 H308 Z" fill="#E0402B"/><ellipse cx="326" cy="91" rx="9" ry="3.5" fill="#fff" fill-opacity=".5"/>'
    + spoj(224, 90) + spoj(264, 110)
    + note(65, 51, 65, 34, 'vypínač', 'middle')
    + '<text class="hint" x="140" y="70">červený: plus</text><text class="hint" x="140" y="136">černý: mínus</text>'
    + note(262, 88, 262, 60, 'delší nožka', 'middle')
    + note(284, 112, 284, 140, 'kratší nožka', 'middle')
    + note(304, 72, 330, 52, 'okraj přečnívá na straně plusu')
    + note(341, 100, 360, 100, 'LED')
    + note(66, 138, 66, 160, 'box s knoflíkovou baterií', 'middle'),
    'Zapojení ozdoby: červený vodič z boxu (plus) k delší nožce LED, černý (mínus) ke kratší. Tečky jsou pájené spoje, každý se pak omotá izolepou, aby se nedotkly.',
    '0 20 400 160')

ozdoba = (
    # zepředu: hvězda, uprostřed svítící LED v kapce lepidla, nahoře provázek
    hvezda(110, 128, 82, 34)
    + kabel('M110 62 C96 40 96 22 110 18 C124 22 124 40 110 62', '#B8331F', 2)
    + '<circle cx="110" cy="62" r="3" fill="#fff" stroke="#9C7442" stroke-width="1"/>'
    + '<circle cx="80" cy="150" r="5" fill="#E8487A"/><circle cx="140" cy="150" r="5" fill="#13A39A"/><circle cx="110" cy="96" r="4" fill="#2F6FE0"/>'
    + paprsky(110, 128, 19, 29, range(-150, 210, 60))
    + '<ellipse cx="110" cy="128" rx="14" ry="13" fill="#EEF5FA" fill-opacity=".8" stroke="#93A9BF" stroke-width="1.1"/>'
    + '<circle cx="110" cy="128" r="8" fill="#E0402B"/><circle cx="107" cy="125" r="2.5" fill="#fff" fill-opacity=".6"/>'
    + note(124, 133, 180, 196, 'LED s kapkou lepidla', odstup=4)
    + note(118, 30, 150, 22, 'provázek')
    + '<text class="lbl" x="110" y="226" text-anchor="middle">zepředu</text>'
    # zezadu: hvězda, nožky LED otvorem, box přilepený tavnou pistolí
    + hvezda(330, 128, 82, 34)
    + kabel('M330 62 C316 40 316 22 330 18 C344 22 344 40 330 62', '#B8331F', 2)
    + '<circle cx="330" cy="62" r="3" fill="#fff" stroke="#9C7442" stroke-width="1"/>'
    + glue(312, 140, 348, 170)
    + '<rect x="312" y="140" width="36" height="30" rx="4" fill="#23272E"/>'
    + '<rect x="324" y="169" width="12" height="6" rx="1" fill="#4A515C"/>'
    + '<circle cx="330" cy="112" r="9" fill="#B8331F"/>'
    + kabel('M333 113 C346 116 346 126 340 140', CERVENA, 2.5) + kabel('M327 113 C314 116 314 126 320 140', CERNA, 2.5)
    + izolepa(337, 117, 9, 8) + izolepa(314, 117, 9, 8)
    + note(352, 152, 392, 156, 'box přilepený', odstup=4) + '<text class="lbl" x="396" y="174">tavnou pistolí</text>'
    + note(337, 176, 372, 202, 'vypínač')
    + note(339, 108, 378, 78, 'LED zezadu')
    + '<text class="lbl" x="330" y="226" text-anchor="middle">zezadu</text>'
)
NAKRESY['ozdoba'] = svg(38, ozdoba,
    'Hotová ozdoba. Zepředu svítí LED prostrčená otvorem v kartonu, kapka tavného lepidla rozptýlí světlo. Zezadu je přilepený box s baterií, spoje jsou omotané izolepou.',
    '0 8 470 228')


# --- hlavolam s pamětí: zapojení s relé zespodu, součástky jak vypadají ---
def drzak(x, y, w, h, text):
    """Kryt na tužkové baterie shora, vývody vpravo."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#3B4A63"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 4}" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{text}</text>')
def bzucak(x, y):
    """Bzučák z boku, plusová (delší) nožka vlevo v x + 10, mínusová v x + 30; tělo 40 × 26 od (x, y)."""
    return (f'<line x1="{x + 10}" y1="{y + 26}" x2="{x + 10}" y2="{y + 66}" {NOZKA}/>'
            f'<line x1="{x + 30}" y1="{y + 26}" x2="{x + 30}" y2="{y + 60}" {NOZKA}/>'
            f'<rect x="{x}" y="{y}" width="40" height="26" rx="4" fill="#1B2B4B"/>'
            f'<text x="{x + 10}" y="{y + 18}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">+</text>')
def dioda(x1, x2, y):
    """Dioda naležato, černé tělo, šedý proužek u levého konce (x1)."""
    return (f'<rect x="{x1}" y="{y - 5}" width="{x2 - x1}" height="10" rx="3" fill="#1B1B1B"/>'
            f'<rect x="{x1 + 3}" y="{y - 5}" width="4" height="10" fill="#C9D2DE"/>')

# relé SRD-05VDC zespodu: COM u kraje, vedle něj dva vývody cívky, na druhém konci NO a NC
RX, RY = 291, 110
PIN = {'com': (345, 120), 'c1': (303, 134), 'c2': (387, 134), 'no': (303, 219), 'nc': (387, 219)}
rele_zespodu = (
    f'<rect x="{RX}" y="{RY}" width="108" height="133" rx="5" fill="{RELE}"/>'
    f'<rect x="{RX + 5}" y="{RY + 5}" width="98" height="123" rx="3" fill="#2A2F38"/>'
    + ''.join(f'<rect x="{x - 4}" y="{y - 2}" width="8" height="4" fill="#C3CAD3"/>' for x, y in PIN.values())
)
hlavolam_rele_zapojeni = (
    drzak(20, 40, 90, 40, '2× AA') + drzak(20, 110, 50, 26, '1× AA')
    + vypinac_bok(140, 46) + bzucak(200, 150) + rele_zespodu
    # baterie za sebou: mínus krytu 2× AA na plus krytu 1× AA
    + kabel('M110 70 C134 70 126 116 70 116', MODRA, 3)
    + kabel('M110 50 C124 50 128 54 140 54', CERVENA, 3)
    # za vypínačem: lanko k dráze a lanko na COM
    + kabel('M162 54 C196 54 206 40 240 40 H440', CERVENA, 3)
    + kabel('M162 54 C240 60 345 62 345 120', CERVENA, 3)
    # mínus krytu 1× AA na levý vývod cívky a z něj na kratší nožku bzučáku
    + kabel('M70 130 C140 112 250 124 303 134', MODRA, 3)
    + kabel('M303 134 C272 150 236 170 230 210', MODRA, 3)
    # pravý vývod cívky spojený s pravým NO; odtud na delší nožku bzučáku, kde je i lanko od očka
    + kabel('M387 134 H405 Q415 134 415 144 V209 Q415 219 405 219 H387', ORANZOVA, 3)
    + kabel('M387 219 C387 262 360 264 300 264 H232 C216 264 210 240 210 216', ORANZOVA, 3)
    + kabel('M210 216 C196 252 90 252 40 252', ORANZOVA, 3)
    # dioda přímo na vývodech cívky, proužek k plusu (vpravo)
    + '<path d="M303 134 L325 180 M365 180 L387 134" fill="none" stroke="#9AA6B8" stroke-width="2"/>'
    + '<rect x="325" y="175" width="40" height="10" rx="3" fill="#1B1B1B"/><rect x="355" y="175" width="4" height="10" fill="#C9D2DE"/>'
    + ''.join(spoj(x, y, 3.5) for x, y in ((110, 50), (110, 70), (70, 116), (70, 130), (162, 54), (210, 216), (230, 210)))
    + ''.join(spoj(*PIN[k], 3.5) for k in ('com', 'c1', 'c2', 'nc'))
    + '<text class="lbl" x="303" y="104" text-anchor="middle">cívka</text><text class="lbl" x="392" y="104" text-anchor="middle">cívka</text>'
    + '<text x="352" y="126" font-size="10" font-weight="700" fill="#fff">COM</text>'
    + '<text x="303" y="238" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">NO</text>'
    + '<text x="387" y="238" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">NO</text>'
    + '<text class="hint" x="303" y="256" text-anchor="middle">stačí jeden NO</text>'
    + note(366, 186, 424, 196, 'dioda', odstup=3) + '<text class="hint" x="428" y="212">proužek k plusu</text>'
    + note(151, 61, 151, 82, 'vypínač', 'middle') + note(199, 160, 178, 150, 'bzučák', 'end')
    + '<text class="lbl" x="444" y="44">k dráze</text><text class="lbl" x="36" y="268">k očku</text>'
)
NAKRESY['hlavolam-rele-zapojeni'] = svg(39, hlavolam_rele_zapojeni,
    'Zapojení s relé podle schématu, relé je nakreslené zespodu. Za vypínačem vede lanko k dráze a lanko na COM. Lanko od očka, jeden vývod NO a jeden vývod cívky jsou na delší nožce bzučáku. Kratší nožka bzučáku a druhý vývod cívky vedou k mínusu krytu na 1× AA. Dioda je připájená přímo na vývody cívky, proužkem k plusu.',
    '0 14 520 270')


# --- hlavolam s pamětí z tranzistorů: modul od vedoucího, BC557 + BC547 a čtyři odpory ---
R10K = ('#8B4A1C', '#1B1B1B', '#F08A24')
R4K7 = ('#E9B425', '#7B3FB0', '#E0402B')
def odpor_vodorovne(x1, x2, y, pruhy):
    p = ''.join(f'<rect x="{x1 + 5 + 6 * i}" y="{y - 6}" width="3" height="12" fill="{b}"/>' for i, b in enumerate(pruhy))
    return (f'<rect x="{x1}" y="{y - 6}" width="{x2 - x1}" height="12" rx="5" fill="#E8D3A8" stroke="#A88B5A" stroke-width="1"/>'
            + p + f'<rect x="{x2 - 9}" y="{y - 6}" width="3" height="12" fill="#C9A23A"/>')
def to92(x, y, nozky_vpravo, nazev):
    """Tranzistor TO-92 plochou stranou k nám, otočený nožkami do strany; tělo 30 × 40 od (x, y)."""
    # zaoblená strana je odvrácená od nožek, rovná strana je u nožek
    d = (f'M{x + 30} {y} H{x + 10} Q{x} {y} {x} {y + 10} V{y + 30} Q{x} {y + 40} {x + 10} {y + 40} H{x + 30} Z' if nozky_vpravo
         else f'M{x} {y} H{x + 20} Q{x + 30} {y} {x + 30} {y + 10} V{y + 30} Q{x + 30} {y + 40} {x + 20} {y + 40} H{x} Z')
    return (f'<path d="{d}" fill="#23272E"/>'
            f'<text transform="translate({x + 18} {y + 20}) rotate(-90)" text-anchor="middle" font-size="9" font-weight="700" fill="#B7C0CB">{nazev}</text>')
def drat(d):
    return f'<path d="{d}" fill="none" stroke="#9AA6B8" stroke-width="2.5" stroke-linejoin="round"/>'

modul = (
    # PNP vlevo, nožky doprava: shora E, B, C
    to92(50, 80, True, 'BC557')
    + drat('M80 92 L110 60 H162') + drat('M80 100 H162') + drat('M80 108 L110 140 H162')
    # NPN vpravo, nožky doleva: shora C, B, E
    + to92(340, 120, False, 'BC547')
    + drat('M340 132 L310 100 H300') + drat('M340 140 H300') + drat('M340 148 L310 180 H300')
    # odpory: 10k mezi E a B PNP, 4k7 z B PNP do X, 4k7 z C PNP do B NPN, 10k mezi B a E NPN
    + drat('M162 60 V100') + odpor_svisle(162, 66, 94, R10K)
    + drat('M162 100 H300') + odpor_vodorovne(196, 232, 100, R4K7)
    + drat('M162 140 H300') + odpor_vodorovne(196, 232, 140, R4K7)
    + drat('M300 140 V180') + odpor_svisle(300, 146, 174, R10K)
    # tři lanka ven
    + kabel('M162 60 V32 H420', CERVENA, 3.5) + kabel('M300 100 V72 H420', ORANZOVA, 3.5) + kabel('M300 180 V208 H420', MODRA, 3.5)
    + ''.join(spoj(x, y, 4) for x, y in ((162, 60), (162, 100), (162, 140), (300, 100), (300, 140), (300, 180)))
    + ''.join(f'<text class="hint" x="{x}" y="{y}" text-anchor="middle">{t}</text>' for x, y, t in
              ((124, 55, 'E'), (124, 95, 'B'), (124, 135, 'C'), (322, 95, 'C'), (322, 135, 'B'), (322, 175, 'E')))
    + '<text class="lbl" x="44" y="96" text-anchor="end">PNP</text><text class="hint" x="44" y="110" text-anchor="end">BC557</text>'
    + '<text class="lbl" x="376" y="136">NPN</text><text class="hint" x="376" y="150">BC547</text>'
    + '<text class="lbl" x="152" y="84" text-anchor="end">10 kΩ</text><text class="lbl" x="214" y="90" text-anchor="middle">4,7 kΩ</text>'
    + '<text class="lbl" x="214" y="162" text-anchor="middle">4,7 kΩ</text><text class="lbl" x="290" y="164" text-anchor="end">10 kΩ</text>'
    + '<text class="lbl" x="424" y="36">+</text><text class="hint" x="416" y="26" text-anchor="end">k delší nožce bzučáku</text>'
    + '<text class="lbl" x="424" y="76">X</text><text class="hint" x="416" y="66" text-anchor="end">ke kratší nožce bzučáku</text>'
    + '<text class="lbl" x="424" y="212">−</text><text class="hint" x="416" y="224" text-anchor="end">k mínusu baterií</text>'
)
NAKRESY['hlavolam-tranzistory-modul'] = svg(40, modul,
    'Modul paměti ze dvou tranzistorů. Tranzistory leží plochou stranou s nápisem nahoru. Odpory 10 kΩ (hnědá, černá, oranžová) drží tranzistory v klidu zavřené, přes odpory 4,7 kΩ (žlutá, fialová, červená) se navzájem otevírají. Tři lanka vedou k hlavolamu.',
    '0 14 440 218')

# schéma hlavolamu s modulem z tranzistorů, ve stejném stylu jako schéma s relé
def tranzistor_zn(cx, cy, baze_vlevo, pnp):
    """Schematická značka tranzistoru: báze z boku, kolektor a emitor vycházejí nahoru a dolů."""
    d = 1 if baze_vlevo else -1
    bx, lx = cx - 7 * d, cx + 7 * d
    e = ((lx, cy - 13), (bx, cy - 5)) if pnp else ((bx, cy + 5), (lx, cy + 13))  # šipka emitoru: od, k
    (ax, ay), (tx, ty) = e
    dx, dy = tx - ax, ty - ay
    delka = math.hypot(dx, dy)
    ux, uy = dx / delka, dy / delka
    kx, ky = ax + ux * delka * .85, ay + uy * delka * .85
    hrot = (f'{kx:.1f},{ky:.1f} {kx - 7 * ux - 3.5 * uy:.1f},{ky - 7 * uy + 3.5 * ux:.1f} '
            f'{kx - 7 * ux + 3.5 * uy:.1f},{ky - 7 * uy - 3.5 * ux:.1f}')
    return (f'<circle cx="{cx}" cy="{cy}" r="18" fill="#fff" stroke="#1B2B4B" stroke-width="2"/>'
            f'<line x1="{bx}" y1="{cy - 11}" x2="{bx}" y2="{cy + 11}" stroke="#1B2B4B" stroke-width="3.5"/>'
            f'<polyline points="{bx},{cy - 5} {lx},{cy - 13} {lx},{cy - 18}" fill="none" stroke="#1B2B4B" stroke-width="2"/>'
            f'<polyline points="{bx},{cy + 5} {lx},{cy + 13} {lx},{cy + 18}" fill="none" stroke="#1B2B4B" stroke-width="2"/>'
            f'<polygon points="{hrot}" fill="#1B2B4B"/>')
def odpor_zn(x, y1, y2):
    """Schematická značka odporu na svislém vodiči."""
    return f'<rect x="{x - 5}" y="{y1}" width="10" height="{y2 - y1}" fill="#fff" stroke="#1B2B4B" stroke-width="2.5"/>'

hlavolam_tranzistory = (
    # vypínač zapnutý, bzučák a pod ním očko ~ dráha
    vodic('30,95 30,30 150,30') + '<circle cx="55" cy="30" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/><circle cx="85" cy="30" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/>'
    + vodic('120,30 120,150') + vodic('120,180 120,210') + vodic('30,119 30,210 310,210')
    + '<rect x="111" y="55" width="18" height="30" rx="3" fill="#fff" stroke="#1B2B4B" stroke-width="2.5"/><text class="lbl" x="115" y="67" style="font-size:10px">+</text>'
    + f'<line x1="120" y1="180" x2="106" y2="153" stroke="{MED}" stroke-width="2.5" stroke-linecap="round"/>'
    + '<circle cx="120" cy="150" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/><circle cx="120" cy="180" r="3" fill="#fff" stroke="#1B2B4B" stroke-width="1.5"/>'
    # baterie: jen kryt na 2× AA
    + '<rect x="12" y="87" width="36" height="40" rx="5" fill="none" stroke="#9AA6B8" stroke-width="1.2" stroke-dasharray="3 3"/>'
    + '<g stroke="#1B2B4B" stroke-linecap="round">'
    + ''.join(f'<line x1="18" y1="{y}" x2="42" y2="{y}" stroke-width="2.5"/><line x1="24" y1="{y + 7}" x2="36" y2="{y + 7}" stroke-width="4"/>'
              for y in (95, 112)) + '</g>'
    + vodic('30,102 30,112') + '<text class="lbl" x="52" y="97">+</text>'
    + '<text class="lbl" x="7" y="111" text-anchor="end">2× AA</text><text class="hint" x="7" y="129" text-anchor="end">= 3 V</text>'
    # modul: tři vývody +, X a −
    + '<rect x="148" y="18" width="212" height="204" rx="8" fill="none" stroke="#9AA6B8" stroke-width="1.2" stroke-dasharray="5 4"/>'
    + vodic('150,30 252,30 252,57') + vodic('120,120 255,120 255,147') + vodic('255,183 255,210')
    + vodic('180,30 180,120') + odpor_zn(180, 40, 64) + odpor_zn(180, 86, 110) + vodic('180,75 238,75')
    + vodic('252,93 252,100 310,100 310,210') + odpor_zn(310, 118, 146) + odpor_zn(310, 176, 200) + vodic('269,165 310,165')
    + tranzistor_zn(245, 75, True, True) + tranzistor_zn(262, 165, False, False)
    + uzel(120, 30) + uzel(120, 120) + uzel(120, 210) + uzel(180, 30) + uzel(180, 75) + uzel(180, 120)
    + uzel(255, 120) + uzel(255, 210) + uzel(310, 165)
    + f'<text class="lbl" x="156" y="46" style="fill:{CERVENA}">+</text>'
    + f'<text class="lbl" x="156" y="114" style="fill:{ORANZOVA}">X</text>'
    + f'<text class="lbl" x="156" y="204" style="fill:{MODRA}">−</text>'
    + '<text class="lbl" x="190" y="56">10 kΩ</text><text class="lbl" x="190" y="102">4,7 kΩ</text>'
    + '<text class="lbl" x="318" y="136">4,7 kΩ</text><text class="lbl" x="318" y="192">10 kΩ</text>'
    + '<text class="lbl" x="274" y="70">PNP</text><text class="hint" x="274" y="84">BC557</text>'
    + '<text class="lbl" x="236" y="168" text-anchor="end">NPN</text><text class="hint" x="236" y="182" text-anchor="end">BC547</text>'
    + '<text class="lbl" x="70" y="14" text-anchor="middle">vypínač = reset</text>'
    + '<text class="lbl" x="254" y="12" text-anchor="middle">modul od vedoucího</text>'
    + '<text class="lbl" x="104" y="74" text-anchor="end">bzučák</text>'
    + f'<text class="lbl" x="102" y="164" text-anchor="end" style="fill:{MED_TMAVA}">očko</text>'
    + f'<text class="lbl" x="102" y="178" text-anchor="end" style="fill:{MED_TMAVA}">~ dráha</text>'
)
NAKRESY['hlavolam-tranzistory'] = svg(42, hlavolam_tranzistory,
    'Schéma s modulem z tranzistorů v klidu, vypínač je zapnutý. Stačí kryt na 2× AA. Modul má tři vývody: + na delší nožku bzučáku, X na kratší nožku a − na mínus baterií. Tranzistor NPN je zapojený vedle očka a dráhy: když se otevře, vede proud místo nich.',
    '-40 0 410 230')

def nozka_3d(x, kx):
    """Nožka zespodu tranzistoru: u těla širší ramínko, pak tenký drát, který se lehce rozbíhá ke kx."""
    return (f'<path d="M{x - 3.5} 100 H{x + 3.5} V112 L{x + 1.8} 116 H{x - 1.8} L{x - 3.5} 112 Z" fill="#AEB6C1"/>'
            f'<path d="M{x - 1.8} 116 L{kx - 1.8} 204 H{kx + 1.8} L{x + 1.8} 116 Z" fill="#C3CAD3"/>'
            f'<path d="M{x + 0.6} 116 L{kx + 0.6} 204 H{kx + 1.8} L{x + 1.8} 116 Z" fill="#8A939F"/>')
NAKRESY['tranzistor-nozky'] = svg(41,
    # úzký kulatý bok vpravo, spodní plocha, ze které vycházejí nožky
    '<path d="M214 22 Q221 24 223 30 V95 Q220 93 214 92 Z" fill="#3A414B"/>'
    + '<path d="M160 92 H214 Q221 93 223 95 C222 104 204 109 188 109 C172 109 160 102 160 92 Z" fill="#4A515C"/>'
    + ''.join(nozka_3d(x, kx) for x, kx in ((174, 170), (190, 190), (206, 210)))
    # plochá strana s nápisem, světlá zaoblená horní hrana
    + '<path d="M160 92 V27 Q160 22 165 22 H209 Q214 22 214 27 V92 Z" fill="#1E2228"/>'
    + '<path d="M161 30 V27 Q161 23 165 23 H209 Q213 23 213 27" fill="none" stroke="#8A939F" stroke-width="1.5"/>'
    + '<text x="187" y="52" text-anchor="middle" font-size="14" font-weight="700" fill="#D5DBE3">BC</text>'
    + '<text x="187" y="70" text-anchor="middle" font-size="14" font-weight="700" fill="#D5DBE3">547</text>'
    + ''.join(f'<text x="{x}" y="222" text-anchor="middle" font-size="16" font-weight="700" fill="#1B2B4B">{t}</text>'
              for x, t in ((170, 'C'), (190, 'B'), (210, 'E')))
    + note(158, 44, 140, 30, 'plochá strana', 'end') + '<text class="lbl" x="136" y="48" text-anchor="end">s nápisem</text>'
    + note(224, 60, 244, 50, 'kulatá strana')
    + '<text class="lbl" x="250" y="140">C kolektor</text><text class="lbl" x="250" y="158">B báze</text><text class="lbl" x="250" y="176">E emitor</text>',
    'Tranzistor plochou stranou s nápisem k sobě, nožky dolů: zleva C, B, E. Platí pro BC547 (NPN) i BC557 (PNP).',
    '40 8 300 222')
