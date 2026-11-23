---
name: nakresy
description: Kreslení a úpravy schematických SVG nákresů pro návody na webu Bastlířské dílny (verejny-web/nakresy.py, v lekcích {{nakres jmeno}}). Použij vždy, když má vzniknout nebo se změnit nákres, obrázek, schéma zapojení, ilustrace kroku nebo popisek v obrázku k lekci, i když uživatel řekne jen „nakresli“, „uprav obrázek“, „posuň tu součástku“ nebo pošle snímek nákresu s výhradou. Shrnuje, co vedoucí kroužku na nákresech dříve opravoval.
---

# Nákresy k návodům

Nákresy čtou děti zhruba od 8 let a jejich rodiče. Mají ukázat, jak věc postavit, ne být technickou dokumentací. Vedoucí kroužku je staví sám a hned pozná, když nákres neodpovídá tomu, jak se to opravdu dělá. Většina dřívějších oprav byla právě o tom.

## Kde co je

- `verejny-web/nakresy.py`: slovník `NAKRESY` s hotovými nákresy a pomocné funkce. Každý nákres vzniká voláním `svg(n, tělo, popisek, viewBox)`.
  - `n` je jedinečné číslo nákresu, protože z něj vznikají id šipek (`sip{n}` a `hrot{n}`). Nový nákres dostane číslo o jedna vyšší, než je dosud nejvyšší (`grep -o "svg([0-9]*" verejny-web/nakresy.py`).
  - Popisek se zobrazí pod obrázkem a zároveň slouží jako `aria-label`.
  - viewBox ořízněte těsně kolem obsahu, ale tak, aby se vešly všechny texty.
- Do lekce (`verejny-web/lekce/NN-adresa.md`) se nákres vloží řádkem `{{nakres jmeno}}`. Na kartě lekce ho ukáže `prehled_nakres: jmeno` v hlavičce.
- Styly jsou v `verejny-web/static/styles.css` (`.diagram`, `.lbl`, `.hint`, `.lead`, `.old`, `.dim`, `.ground`).
- Než začnete kreslit, projděte si pomocné funkce v `nakresy.py` a použijte je, ať nákresy vypadají jednotně:
  - kóty `dim_h` a `dim_v`;
  - popisek se šipkou `note`;
  - lepidlo z tavné pistole `glue`;
  - díly z předchozích kroků vybledle `old`;
  - drát `med` a lanko `kabel`;
  - pájený spoj `spoj`, izolepa `izolepa`, vypínač `vypinac_bok`;
  - baterie `clanek` a pružinka `pruzinka`, držák na dvě tužkové baterie `drzak_2aa`;
  - krokosvorka `krokosvorka`, třetí ruka `treti_ruka`;
  - motorek `motor_bok`, odpor `odpor_svisle`;
  - věž ze špaget: `spag`, `kulicka`, `paska`.

## Postup

1. **Ujasněte si skutečnost.** Jak přesně se ta věc v lekci dělá: čím se lepí, kam se co zasune, která nožka je plus, co se nepoužívá. Vycházejte z karty projektu (`projekty/*.md`), z textu lekce a z toho, co řekl uživatel. Když to nevíte, zeptejte se. Nákres, který vypadá hezky, ale ukazuje jiný postup, je horší než žádný.
2. **Nakreslete** v `nakresy.py` z pomocných funkcí. Když se nějaký prvek opakuje, udělejte z něj funkci.
3. **Sestavte web**: `python3 -B verejny-web/build.py --koncepty`.
4. **Prohlédněte si výsledek v prohlížeči**, a to vždy, než ho ukážete uživateli. Uživatel to výslovně chce („vždycky se na to pořádně podívej, když něco děláš s grafikou“).
   - Servírujte `site/` přes http na volném portu (8765 bývá obsazený, náhled `make nahled` používá 8766). Prohlížeč keší, proto přidávejte `?v=N`.
   - Jeden nákres vyfoťte jako element: `figure.diagram:has(svg text:text("…"))`.
   - Víc nákresů naráz, například po změně pomocné funkce, ukáže `python3 -B .claude/skills/nakresy/scripts/galerie.py [jména]` a pak snímky sekcí `#g0`, `#g1` a další.
   - Nákres v lekci je široký nejvýš 460 px. Když přidáte šířku, celý nákres se zmenší a texty s ním.
5. **Projděte kontrolní seznam níže** a opravte, co nesedí. Teprve potom ukažte výsledek.
6. **Ukliďte** `site/_galerie.html`, složku `.playwright-mcp/` a spuštěný server. Web nasazujte a commitujte, jen když o to uživatel požádá.

## Popisky

- **Popisek ukazuje na místo šipkou** (`note`). Šipka vede od textu k místu a končí těsně před ním (`MEZERA`), takže místo nepřekryje. Na konci není tečka.
- **Cíl šipky (x1, y1) leží na okraji dílu, ne uvnitř.** U kulatých věcí, na jejichž střed míříte, nastavte `odstup=` větší než poloměr. Šipka do středu izolepy nebo do těla zarážky překrývá právě to, co popisuje.
- **Text se vejde do obrázku** a nepřekrývá díly ani jiné texty. Hlídejte levý a pravý okraj viewBoxu a texty s `text-anchor="end"`.
- **Popisujte jen to, co je jisté.** Nejistý nebo nepřesný popisek raději vynechte („nedávat, pokud to není úplně jasné“).
- **Čeština:** krátce, bez odborných slov. Hlídejte pravopis (prkénko, ne prkýnko).

## Věrnost skutečnosti

Co uživatel na dřívějších nákresech opravoval. Berte to jako příklady toho, jak se dívá, nejen jako seznam:

- **Lepení:**
  - tavná pistole lepí po celé délce, proto se kreslí jako vlnka kolem dílu (`glue`), ne jako tečky;
  - lepidlo je jen tam, kde se díly dotýkají: nepřečuhuje přes karton a u zarážky je pod ní, mezi zarážkou a osou.
- **Polohy a rozměry:**
  - díly jsou tam, kde v reálu: háček zasunutý do vlnité vrstvy kartonu, gumička začíná u kartonu, kola těsně u těla auta;
  - měření ukazuje to, co se opravdu měří: dojezd až ke dni, kde auto zastavilo, výšku věže bez kelímku se zátěží.
- **Fyzika:**
  - musí to fungovat, jak je nakresleno: kelímek stojí na rovném vrchním patře, šikmá výztuha jde tím směrem, který při daném pohybu pomůže;
  - spoj dvou špaget se překrývá a drží ho dvě pásky na krajích, které moc nepřečuhují.
- **Úplnost:** ve schématu zapojení nesmí chybět žádná součástka (jednou chyběl vypínač). Naopak nekreslete nic, co se v lekci nepoužívá.
- **Elektronika:**
  - značka plus u bzučáku je u plusové (delší) nožky;
  - baterie v držáku jsou každá obráceně a plochý mínus je u pružinky;
  - plusový konec baterie je hnědý, protože tmavě modrý splýval s pozadím;
  - LED má delší nožku plus a na straně mínusu zkosený okraj. Délka nožek musí být vidět i po zapojení. Když není, přidejte vedle rámeček „zblízka“;
  - součástky mají rozumně dlouhé nožky. Raději odsuňte odpor stranou a nožky ohněte, než aby skoro nebyly vidět.
- **Pájení:**
  - spojované lanko má stejnou barvu izolace na obou stranách;
  - před zakroucením vede drátek kousek holý;
  - háčky jsou do sebe zaháknuté;
  - třetí ruka má dvě části ramene a drát drží jedna krokosvorka;
  - šipka na hrot páječky končí kousek před špičkou, aby byla špička vidět.
- **Volné stavby** (věž, most): nákres ukazuje princip, jak stavět, ne hotový tvar. Nechte prostor pro fantazii dětí.

## Styl

- Vycházejte z barev v `nakresy.py` (`MED`, `MODRA`, `CIN`, `KAR`, `SPEJLE`, `DREVO` a dalších). Červená je plus a lanko k dráze, modrá je mínus a lanko k očku.
- V návodu po krocích je barevné to, co v daném kroku přibude. Díly z předchozích kroků jsou vybledlé (`old`). V jednom návodu držte stejný pohled, třeba vždy zespodu.
- Jednoduché tvary, žádné stíny ani přechody. Malý lesk (bílá elipsa s průhledností) stačí.
- Když drobný detail není v celkovém nákresu čitelný, přidejte vedle čárkovaný rámeček s detailem zblízka.

## Kontrolní seznam před ukázáním

- Odpovídá nákres tomu, jak se věc v lekci opravdu dělá? Chybí něco, nebo tam něco přebývá?
- Je správně polarita a délka nožek, otočení baterií a barvy lanek?
- Končí každá šipka těsně před okrajem dílu, bez tečky a bez překrytí?
- Vejdou se všechny texty, nepřekrývají se a nic není oříznuté?
- Je nákres čitelný v šířce 460 px, tedy ve velikosti, jakou má na webu?
- Prohlédli jste si ho opravdu v prohlížeči, ne jen v kódu?
