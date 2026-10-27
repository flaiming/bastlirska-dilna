# Bastlířská dílna

Poznámky a návody pro školní technický kroužek pro děti z 3.–5. třídy. Děti staví jednoduché výrobky, zkoušejí pokusy a samy zjišťují, proč věci fungují: autíčko na gumičku, věže ze špaget, drátěný hlavolam s bzučákem, vibrobot z kartáče, první elektronika s LED a tranzistory.

Kroužek běží každé úterý dvě hodiny, dvě skupiny po 8–9 dětech se střídají ob týden a vede ho jeden dospělý. Návody jsou psané tak, aby to zvládl jeden člověk s devíti dětmi a malým rozpočtem.

## Co tu je

| Soubor | Obsah |
| --- | --- |
| [README_Bastlirska_dilna.md](README_Bastlirska_dilna.md) | Hlavní přehled: zásobník témat, plán lekcí, termíny, koncepce elektro lekcí |
| [projekty/](projekty/README.md) | Projektové karty: cíl, příprava vedoucího, materiál, postup na dvě hodiny, ladění, bezpečnost, zkušenosti po lekci |
| [NAKUPNI_ZAKLAD.md](NAKUPNI_ZAKLAD.md) | Sklad, nákupy podle obchodů, co si děti odnesou a co zůstává v dílně |
| [modely/](modely/) | 3D modely pro tisk (OpenSCAD + STL), např. excentr pro vibrobota |
| [web/](web/) | Generátor HTML přehledu z Markdownu |
| [verejny-web/](verejny-web/) | Zdroje veřejného webu [bastleni.oram.cz](https://bastleni.oram.cz) |

## Projektové karty

Každá karta vychází ze [šablony](projekty/SABLONA.md) a po odučení se doplňuje o to, co fungovalo a co změnit pro druhou skupinu. Přehled karet a jejich stav je v [projekty/README.md](projekty/README.md).

## Veřejný web

Web [bastleni.oram.cz](https://bastleni.oram.cz) ukazuje jen odučené lekce s návodem. Skládá se z Markdownu ve `verejny-web/`, výstup jde do `site/` (není v gitu).

```sh
make web       # sestaví site/
make nahled    # sestaví a pustí na http://localhost:8765
make nasadit   # sestaví a nahraje na server
make fotka Z=~/Downloads/IMG_1234.jpg JAKO=auto-novy [OTOCIT=90]   # zmenší fotku a odstraní metadata
```

- Nová lekce je jeden soubor `verejny-web/lekce/NN-adresa.md`. Formát je popsaný na začátku `verejny-web/build.py`, nejlíp je zkopírovat existující lekci. Lekci pak smažte z „Co chystáme dál“ v `verejny-web/domu.md`.
- Fotky leží ve `verejny-web/static/foto/` a každá má popisek ve `verejny-web/fotky.txt`. Na fotkách nesmí být obličej dítěte.
- Nákresy ke krokům jsou ve `verejny-web/nakresy.py`, do textu se vkládají řádkem `{{nakres jmeno}}`.
- K odkazům na fotky, styly a modely build přidá otisk obsahu (`?v=…`), takže prohlížeč po změně nenačte starou verzi.
- Konfigurace nginx na serveru je pro přehled ve `verejny-web/nginx.conf`.

## HTML přehled

```sh
python3 web/build.py
```

Složí `web/index.html` z `web/template.html`, hlavního přehledu, nákupního základu a projektových karet. Stránka nepotřebuje server, Markdown se vykreslí v prohlížeči. Plán lekcí, termíny a rychlé odkazy jsou přímo v `web/build.py`.

## 3D modely

```sh
openscad -D 'dil="excentr"' -o modely/excentr.stl modely/excentr.scad
openscad -D 'dil="zkouska"' -o modely/excentr_zkouska.stl modely/excentr.scad
```

Rozměry (otvor pro hřídel, poloměr závaží) se mění parametry na začátku `.scad` souboru.

## Použití a licence

Návody klidně použijte, upravte a sdílejte pro vlastní kroužek nebo hodinu. Ceny a odkazy na obchody odpovídají stavu v době zápisu (podzim 2026), před nákupem je ověřte.

Obsah repozitáře (návody, modely i skripty) je pod licencí [Creative Commons Uveďte původ 4.0 Mezinárodní (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.cs), plné znění v souboru [LICENSE](LICENSE). Stačí uvést „Bastlířská dílna“ s odkazem na tento repozitář a napsat, co jste změnili.
