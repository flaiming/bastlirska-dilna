---
adresa: drateny-hlavolam-2
barva: spaghetti
nazev: Drátěný hlavolam 2
popis: Dokončení drátěného hlavolamu: dráha, očko a hra. Pro rychlé světlo k pípání a hlavolam s pamětí.
perex: Obvod s bzučákem máme zapájený z minula. Teď ohneme dráhu, připájíme očko a zahrajeme si. Kdo bude hotový dřív, přidá k pípání světlo.
kdy: skupina B 24. listopadu, skupina A 1. prosince 2026
jak_dlouho: 2 hodiny
domu: hotový hlavolam bez baterií, doma stačí vložit 2 tužkové baterie
zverejnit: 2026-11-23
prehled: Obvod s bzučákem z minulé lekce dostane dráhu a očko a hlavolam je hotový. Kdo je rychlý, přidá k bzučáku LED, která se při dotyku rozsvítí.
prehled_kdy: Skupina B 24. listopadu, skupina A 1. prosince 2026.
prehled_nakres: hlavolam-led
tlacitko: Návod na pokračování
---

## Proč LED potřebuje odpor {princip}

LED je malé světélko. Svítí, jen když jím teče proud správným směrem: od delší nožky (plus) ke kratší (mínus). Obráceně proud nepustí a zůstane zhasnutá.

Přímo na baterii by LED vzala tolik proudu, že by se přehřála a zničila. Proto se k ní přidává odpor. Ten proud přibrzdí, jako když trochu přivřete kohoutek. S odporem 100 Ω teče LED tak akorát, aby pěkně svítila.

## Co budete potřebovat {potreby}

- Obvod z minula: držák baterií, vypínač, bzučák a dvě volná lanka
- Holý měděný drát 1,5 až 2 mm: 60 cm na dráhu a 20 cm na očko
- Prkénko asi 25 × 8 cm se dvěma otvory 20 cm od sebe
- Izolepu
- Tavnou pistoli
- Kleště a štípačky
- Fixu na namotání očka
- Páječku a cín, viz [návod na pájení](/drateny-hlavolam/#pajeni)

## Dokončení hlavolamu {postup}

Jak se pájí a jak zacházet s páječkou, najdete v [návodu na první část](/drateny-hlavolam/).

### Vyzkoušejte obvod z minula

Vložte baterie: plochý konec baterie (mínus) patří k pružince. Zapněte vypínač a spojte holé konce obou lanek. Bzučák musí pípnout. Když nepípá, podívejte se do [rad níže](#opravy).

### Ohněte dráhu

Drát ohýbejte rukama a v ostrých místech kleštěmi. Udělejte vlny, kopce nebo smyčku, jen ne moc ostré zatáčky, očko by jimi neprošlo. Konce nechte rovné a dlouhé asi 5 cm, zastrčí se do prkénka. Oba konce omotejte asi 3 cm izolepy.

{{nakres hlavolam}}

### Ohněte očko

Konec 20cm drátu omotejte kolem fixy a vzniklé očko trochu rozevřete, aby mělo mezeru. Mezerou ho nasadíte na hotovou dráhu. Z rovného konce je rukojeť.

{{nakres ocko}}

> Čím menší očko, tím těžší hlavolam. Na první pokus bohatě stačí 2 cm.

### Sestavte hlavolam

Konce dráhy zastrčte do otvorů v prkénku a zalepte tavnou pistolí. Červené lanko od bzučáku připájejte ke konci dráhy těsně nad prkénkem. Modré lanko od mínusu baterie připájejte na konec rukojeti očka a rukojeť omotejte izolepou. Obvod přilepte na prkénko, nožky bzučáku ale nechte bez lepidla, ať se k nim dá později připájet světlo. Lepí se jen u stolu s vedoucím.

{{nakres zapojeni}}

### Zahrajte si

Zapněte vypínač a dotkněte se očkem dráhy. Bzučák musí pípnout. Pak očko položte na izolepu na startu a zkuste dojet do cíle bez pípnutí. Kdo to dá nejrychleji? A kdo projede bez jediného pípnutí?

## Na světlo budete potřebovat {potreby}

- Hotový hlavolam
- LED červenou, žlutou nebo zelenou
- Odpor 100 Ω, má proužky hnědý, černý, hnědý
- Kousek lanka asi 5 cm
- Páječku a cín

## Světlo k pípání {postup #svetlo}

Kdo má hlavolam hotový, přidá k bzučáku LED. Při dotyku pak hlavolam pípne a zároveň se rozsvítí. Všechno se pájí na nožky bzučáku, kde už jsou lanka z minula.

Než začnete, vyndejte baterie a sundejte izolepu ze spojů na nožkách bzučáku. Na izolepu ani na lepidlo páječkou nesahejte, taví se a smrdí. Po připájení spoje znovu omotejte izolepou.

### Připájejte odpor

Jednu nožku odporu připájejte k delší nožce bzučáku, kde je lanko od vypínače. U odporu na otočení nezáleží.

{{nakres hlavolam-led}}

### Připájejte LED

Delší nožka LED je plus, kratší je mínus a na její straně má LED zkosený okraj. Delší nožku LED připájejte na druhou nožku odporu. Kratší nožku LED spojte kouskem lanka s kratší nožkou bzučáku, kde vede lanko k dráze. Holé nožky se nesmí dotýkat jiných nožek ani drátů, jinak omotejte izolepou.

### Vyzkoušejte

Dotkněte se očkem dráhy. Bzučák pípne a LED se rozsvítí. Když nesvítí, je LED nejspíš otočená obráceně.

> Použijte červenou, žlutou nebo zelenou LED, ty s odporem 100 Ω na dvě baterie svítí dobře. Bílá a modrá potřebují skoro 3 V, tolik co celé dvě baterie, takže svítí slabě nebo vůbec a menší odpor už moc nepomůže.

> Bez bzučáku jde hlavolam postavit jen se světlem: LED s odporem se zapojí místo bzučáku. Hlavolam pak nepípá, ale svítí.

## Bonus: hlavolam s pamětí {#bonus}

Pro ty, kdo budou hotoví dřív. Obyčejný hlavolam pípá jen během dotyku. Hlavolam s pamětí pípá dál, dokud ho nevypnete, takže nikdo nezapře, že se dotkl. Paměť umí relé, nebo dva tranzistory. Relé máme jen šest, ostatní dostanou modul s tranzistory.

### S relé

Relé je vypínač, který ovládá elektromagnet. Když cívkou relé teče proud, přitáhne kovový jazýček a ten sepne kontakt. Je to slyšet jako cvaknutí.

{{nakres hlavolam-rele}}

- **Dotyk:** očko se dotkne dráhy a proud teče do cívky a do bzučáku. Relé cvakne a sepne svůj kontakt.
- **Drží samo:** kontakt relé je zapojený vedle očka a dráhy. Proud jím teče dál, i když očko z dráhy zvednete, takže cívka si kontakt drží sama.
- **Reset:** vypínač proud přeruší, relé kontakt pustí a je ticho. Po zapnutí se hraje znovu.
- **Napájení 4,5 V:** relé na 5 V na dvě baterie nesepne. Proto se za kryt na 2× AA zapojí ještě kryt na jednu baterii: mínus krytu na dvě baterie se spojí s plusem krytu na jednu. Dohromady dají tři baterie 4,5 V.
- **Co je potřeba:** relé s cívkou na 5 V (například SRD-05VDC), kryt na 1× AA s baterií navíc, dioda 1N4007 a pár kousků lanka. Dioda není nutná, ale chrání před napěťovou špičkou, kterou cívka udělá při vypnutí.

Relé má vespod pět vývodů. Na jednom konci je u kraje COM a vedle něj dva vývody cívky. Na druhém konci jsou dva vývody NO: bez proudu není spojený ani jeden, po cvaknutí se s COM spojí. Stačí zapojit jeden z nich.

Hlavolam s relé se zapojuje podle schématu, tedy trochu jinak než základní: za vypínačem je dráha a bzučák je až za očkem.

- **Baterie:** mínus krytu na 2× AA spojte s plusem krytu na 1× AA.
- **Dráha:** lanko k dráze vede od vypínače. Od vypínače vede i lanko na COM relé.
- **Očko:** lanko od očka připájejte na delší nožku bzučáku. Na ni vede i lanko od jednoho vývodu cívky a od vývodu NO.
- **Mínus:** kratší nožku bzučáku a druhý vývod cívky spojte s mínusem krytu na 1× AA.
- **Dioda:** připájejte ji přímo na vývody cívky, proužkem k vývodu od delší nožky bzučáku.

{{nakres hlavolam-rele-zapojeni}}

> Vyzkoušeli jsme to: relé SRD-05VDC na 4,5 V spolehlivě cvakne a bzučák vydrží i 5 V. Na samotné dvě baterie relé nesepne. Cívka bere hodně proudu, takže hlavolam s relé po hře vypínejte.

### S tranzistory

Tranzistor je elektronický vypínač bez pohyblivých částí. Malý proud do jeho prostřední nožky, báze, pustí velký proud mezi dvěma dalšími nožkami. Modul paměti má dva tranzistory, které se po dotyku navzájem drží otevřené. Stačí mu dvě baterie a v klidu nebere skoro nic.

Modul má hodně drobných spojů, proto ho připraví vedoucí. Vy ho připojíte třemi lanky nebo krokosvorkami:

- **+ (červené):** na delší nožku bzučáku. Je za vypínačem, takže vypínač funguje jako reset.
- **X (oranžové):** na kratší nožku bzučáku, kde začíná lanko k dráze.
- **− (modré):** na mínus krytu baterií, kde začíná lanko k očku.

{{nakres hlavolam-tranzistory}}

{{nakres hlavolam-tranzistory-modul}}

- **Čeká:** odpory 10 kΩ drží oba tranzistory zavřené a neteče nic.
- **Dotyk:** očko spojí X s mínusem a bzučák pípne. Zároveň přes odpor 4,7 kΩ teče malý proud z báze tranzistoru PNP a ten se otevře.
- **Drží:** otevřený PNP pustí proud do báze tranzistoru NPN. Ten se otevře a spojí X s mínusem místo očka. Tranzistory se pak drží otevřené navzájem, i když očko zvednete.
- **Reset:** vypínač proud přeruší a oba tranzistory se zavřou.

Nožky tranzistoru poznáte podle ploché strany s nápisem:

{{nakres tranzistor-nozky}}

> Vyzkoušeli jsme to na dvou bateriích: modul čeká, po dotyku drží a bzučák pípá naplno.

## Když to nefunguje {opravy #opravy}

- **Obvod z minula nepípá** Baterie jsou otočené obráceně, vypínač je vypnutý, bzučák je otočený, nebo některý spoj nevede. Zatáhněte za každý spoj, vedoucí ho může proměřit multimetrem.
- **Pípá pořád** Očko leží na holé dráze, nebo se holý konec lanka dotýká dráhy či baterie.
- **Cín se nechytá dráhy** Drát je špinavý nebo zoxidovaný: obruste ho smirkovým papírem. Pozinkovaný drát se pájí špatně, lanko k němu raději přišroubujte.
- **Očko neprojde zatáčkou** Zatáčku rozevřete, nebo očko zvětšete.
- **Bzučák pípá, LED nesvítí** LED je otočená obráceně, nebo některý spoj u LED nevede. Otočte LED a spoje přepájejte.
- **Po přidání LED bzučák nepípá** Nožky LED nebo odporu se dotýkají nožek bzučáku napřímo. Odtáhněte je od sebe a zaizolujte.
- **LED svítí jen slabě** Je bílá nebo modrá, vyměňte ji za červenou, žlutou nebo zelenou. Nebo jsou slabé baterie.
- **Relé cvakne, ale nedrží** Lanko od NO nevede k delší nožce bzučáku, nebo COM není spojený s vypínačem. Zkontrolujte oba spoje, případně zkuste druhý vývod NO.
- **Relé necvakne** Chybí kryt na 1× AA, nebo jsou slabé baterie. Na dvě baterie relé nesepne.
- **Modul s tranzistory nedrží** Zkontrolujte, že X je na kratší nožce bzučáku a + na delší, a že baterie nejsou slabé.

## Zkuste dál

- Udělejte závod: kdo projede dráhu nejrychleji, ale každé pípnutí přidá 5 vteřin.
- Zkuste projet dráhu levou rukou. Jde to hůř, nebo líp?
- Vyzkoušejte LED různých barev. Která svítí nejvíc?
- Postavte dráhu ve dvou patrech nebo s ostrou spirálou.
