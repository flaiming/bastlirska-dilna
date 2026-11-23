"""Přehled nákresů na jedné stránce, aby šly zkontrolovat všechny najednou.

Použití (z kořene repozitáře):
    python3 -B .claude/skills/nakresy/scripts/galerie.py               # všechny nákresy
    python3 -B .claude/skills/nakresy/scripts/galerie.py hlavolam ocko  # jen vybrané

Zapíše site/_galerie.html (spusťte předtím build.py, aby existoval site/styles.css).
Nákresy jsou po čtyřech v sekcích #g0, #g1, … a každá sekce se vejde na jeden snímek obrazovky.
Stránku servírujte přes http (python3 -m http.server <port> --directory site), file:// prohlížeč neotevře.
Po kontrole soubor smažte, ať se nedostane na web.
"""
import os
import sys

KOREN = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(KOREN, 'verejny-web'))
from nakresy import NAKRESY  # noqa: E402

jmena = sys.argv[1:] or list(NAKRESY)
chybi = [j for j in jmena if j not in NAKRESY]
if chybi:
    sys.exit(f'Neznámé nákresy: {", ".join(chybi)}. Existují: {", ".join(NAKRESY)}')

skupiny = [jmena[i:i + 4] for i in range(0, len(jmena), 4)]
telo = ''.join(
    f'<section id="g{i}" style="display:grid;grid-template-columns:1fr 1fr;gap:8px;width:1200px;margin-bottom:20px">'
    + ''.join(f'<div><b>{j}</b>{NAKRESY[j]}</div>' for j in skupina)
    + '</section>'
    for i, skupina in enumerate(skupiny))
cil = os.path.join(KOREN, 'site', '_galerie.html')
with open(cil, 'w') as f:
    f.write('<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="/styles.css"></head>'
            f'<body style="padding:10px">{telo}</body></html>')
print(f'{cil}: {len(jmena)} nákresů v sekcích #g0 až #g{len(skupiny) - 1}')
