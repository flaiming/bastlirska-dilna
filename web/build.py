#!/usr/bin/env python3
"""Sestaví web/index.html z poznámek kroužku (README, nákupní základ, projektové karty).

Spuštění:  python3 web/build.py
Markdown se vloží do stránky a vykreslí se v prohlížeči (marked.js).
Plán lekcí a termíny níže upravovat ručně, když se změní.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "index.html"
TEMPLATE = Path(__file__).resolve().parent / "template.html"

# Pořadí lekcí pro každou skupinu. card = číslo projektové karty (soubor projekty/NN_*.md).
PLAN = [
    {"n": "1", "title": "Autíčko na gumičku", "card": "03", "status": "done",
     "note": "Odučeno oběma skupinám; zbyl čas i na balónkový pohon."},
    {"n": "2", "title": "Věž a most ze špaget", "card": "13", "status": "next",
     "note": "Stavitelská výzva ve dvojicích + hlasování dětí, kam dál."},
    {"n": "3", "title": "Elektrická dílna I: drátěný hlavolam", "card": "06", "status": "prep",
     "note": "První pájení. Stanoviště: pájení · stavba hlavolamu · Voltík."},
    {"n": "4", "title": "Vibrobot z kartáče", "card": "05", "status": "prep",
     "note": "Prototyp funguje. Pájení k motorku a vypínači, zdobení a závody."},
    {"n": "5–7", "title": "Podle hlasování dětí", "card": None, "status": "idea",
     "note": "Alarm se spouští z kolíčku, světlo na tmu, blikač, vlastní plošný spoj…"},
]

# Úterky do konce 1. pololetí (bez 17. 11. a 29. 12.).
DATES = ["2026-10-20", "2026-10-27", "2026-11-03", "2026-11-10", "2026-11-24",
         "2026-12-01", "2026-12-08", "2026-12-15", "2026-12-22", "2027-01-05",
         "2027-01-12", "2027-01-19", "2027-01-26"]

LINKS = [
    {"t": "Sponkový vypínač a spoušť alarmu", "u": "https://claude.ai/artifact/VuQKH2Ey1gEcUX36jZB9fk",
     "d": "Nákresy a schémata"},
    {"t": "DC motor 18 000 ot/min (Dratek)", "u": "https://dratek.cz/arduino-platforma/2987-dc-motor-3-5v-17-18000rpm.html",
     "d": "Vibrobot, 25 Kč"},
    {"t": "Držák 2× AA DPS DIL (Dratek)", "u": "https://dratek.cz/arduino-platforma/122975-drzak-baterie-2x-aa-dps-dil.html",
     "d": "Hlavolam i vibrobot, 12 Kč"},
    {"t": "Aktivní bzučák 3,3 V (Laskakit)", "u": "https://www.laskakit.cz/aktivni-bzucak-3-3v-5v/?variantId=22805",
     "d": "Hlavolam, 6 Kč"},
    {"t": "Kolébkový vypínač (Dratek)", "u": "https://dratek.cz/arduino-platforma/7699-kolebkovy-vypinac-ac-3a-250v.html",
     "d": "Vibrobot, 4,80 Kč"},
    {"t": "Pastorek 9 zubů (Techfun)", "u": "https://techfun.cz/produkt/ozubene-kolecko-pro-dc-motorky-9-zubu/",
     "d": "Podklad excentru, 5 Kč"},
]


def card_files():
    cards = []
    for p in sorted((ROOT / "projekty").glob("[0-9][0-9]_*.md")):
        md = p.read_text(encoding="utf-8")
        m = re.match(r"#\s+(\d+)\s+(.+)", md)
        cards.append({
            "num": p.name[:2],
            "file": p.name,
            "title": m.group(2).strip() if m else p.stem,
            "md": re.sub(r"^#\s+.+\n", "", md, count=1),
        })
    return cards


def main():
    data = {
        "plan": PLAN,
        "dates": DATES,
        "links": LINKS,
        "cards": card_files(),
        "readme": (ROOT / "README_Bastlirska_dilna.md").read_text(encoding="utf-8"),
        "topics": (ROOT / "projekty" / "README.md").read_text(encoding="utf-8"),
        "shopping": (ROOT / "NAKUPNI_ZAKLAD.md").read_text(encoding="utf-8"),
    }
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", payload)
    OUT.write_text(html, encoding="utf-8")
    print(f"Hotovo: {OUT} ({len(data['cards'])} karet)")


if __name__ == "__main__":
    main()
