# Inspirace: Kroužek elektrotechniky DDM Náměšť nad Oslavou

Web [elektrokrouzek.cz](https://www.elektrokrouzek.cz/cs/clanky) a [GitHub](https://github.com/Elektrokrouzek-cz) kroužku, na který odkazuje [FB skupina vedoucích](fb_vedouci_elektrokrouzku.md). Prošlo se všech 14 článků a 10 aktualit (září 2024 – září 2025). Shrnuto vlastními slovy.

_Staženo: 28. 10. 2026._

## Jak kroužek funguje

- Kroužek začal v září 2024, z velkého zájmu ho rozšířili z 2× 8 na **2× 10 dětí**. Od druhého roku má skupinu začátečníků a dvě skupiny pokročilých, schůzky trvají 1,5 hodiny.
- Vybavení pracovních míst (pájecí stanice, nářadí) zaplatili **sponzoři**, tedy firmy jako Thermo Fisher Scientific nebo Analog Devices a menší podniky. Na webu mají jejich loga. Pro nás: námět, koho oslovit, kdyby nestačil rozpočet.
- Na první schůzce se jen seznamují a probírají bezpečnost, na druhé už začínají první výrobek. Děti si nosí vlastní baterie (3× AA na svítilnu, 2× AAA na další výrobek).
- **Lektor pracuje u svého stolu a webkamera přenáší jeho ruce na velkou televizi.** Všechny děti tak vidí každý krok najednou.
- Na svoje konstrukce nechávají vyrábět plošné spoje a na požádání je poskytnou i jiným kroužkům.

## Nápady pro nás

### Vodní model obvodu: skutečný, ne jen obrázek

Mají „hypermoderní“ přípravek: nádrž na vodu, hadice, dva ventily, průtokoměr s vrtulkou a hrnek na vodu. Ukazují na něm, co děti uvidí v elektrickém obvodu:

| Pokus s vodou | Co z toho plyne v elektřině |
| --- | --- |
| Prázdná nádrž, nic neteče | vybitá baterie, proud neteče |
| Otevřou se oba ventily, voda teče | sepnutý spínač, obvod je uzavřený |
| Druhá nádrž nahoře = vyšší hladina, vrtulka se točí rychleji | vyšší napětí = větší proud |
| Hadice přiškrcená truhlářskou svorkou, voda teče pomaleji | odpor zmenšuje proud |
| Úkol: napustit hrnek přesně do poloviny (bez svorky to nejde stihnout) | proč potřebujeme odpor |
| Čerpadlo místo nádrže, voda se vrací | baterie jako čerpadlo, uzavřený obvod |
| Prázdná druhá nádrž se plní, dokud se hladiny nevyrovnají | nabíjení kondenzátoru (náš „kyblík“) |

Pro nás: v [Součástkách I](../projekty/15_soucastky_led_a_odpor.md) máme „hadicový model“ jen jako vysvětlení. Postavit skutečný přípravek z PET lahví, hadičky, tlačky nebo kolíčku a vrtulky by byl silný úvod do celé elektrické linky. Navíc by se dal použít znovu u kondenzátoru ([Součástky III](../projekty/17_soucastky_kondenzator_a_blikac.md)). Úkol „napusť přesně půl hrnku“ se hodí jako soutěž.

### Webkamera na televizi

Kamera přenáší, co vedoucí dělá rukama, na velkou obrazovku. Jeden vedoucí s devíti dětmi by tak nemusel ukazovat pájení každému zvlášť. Stačí mobil na stojánku a třída s projektorem nebo televizí.

### Svítilna z vodovodní trubky

Jejich první výrobek, který si děti odnášejí domů: kus trubky 23 cm (vnější průměr 32 mm, na teplou vodu), dvě krytky z 3D tiskárny (nahoře LED, dole vypínač) a průhledný kryt na LED. Uvnitř jsou dvě bílé LED, každá se svým odporem 12 Ω, držák 3× AA a tlačítkový vypínač. Spoje se izolují smršťovací bužírkou. Modely krytek ke stažení (OBJ) jsou v [článku](https://www.elektrokrouzek.cz/cs/clanky/konstrukce-svitilna).

Pro nás: opravdu užitečný výrobek na doma, se kterým se dá zacházet i hrubě. Umíme tisknout, takže je to reálné. Krytky by šly upravit na náš držák 2× AA (3 V a jiný odpor). Bužírka se smršťuje nad plamenem, u nás spíš horkovzdušnou pistolí, kterou by obsluhoval vedoucí. Kandidát na výrobek v pájecí dílně (11) nebo na pokračování Součástek I.

### Tranzistorový blikač na kontaktním poli

Dvě LED blikají střídavě jako na železničním přejezdu (astabilní klopný obvod). Součástky: 2× BC547, kondenzátory 47 µF, odpory 470 Ω k LED a 10 kΩ do bází. Napájení 4× AA (6 V). U kondenzátoru a tranzistoru je hezky popsané, jak poznat plus a vývody.

Pro nás: stejné zapojení jako v [Součástkách III](../projekty/17_soucastky_kondenzator_a_blikac.md). My máme 3 V, a proto odpory 47 kΩ a kondenzátory 22 µF. Jejich hodnoty jsou pro 6 V, nekopírovat je.

### Dílenský bateriový zdroj

Čtyři držáky AA připájené na univerzální desku plošných spojů, s barevnými zdířkami na banánky: 0 V, 3 V, 4,5 V a 6 V. Stojí asi 50 Kč, nožičky jsou z 3D tisku. Používají ho na pokusy s kontaktním polem.

Pro nás: máme pravidlo jednoho napětí (3 V), takže se nehodí pro děti. Mohl by ale posloužit vedoucímu u ukázek, třeba k ukázce, že víc voltů znamená jasnější LED.

### Konstrukce na desce plošných spojů (pro starší nebo šikovné děti)

Všechny mají na GitHubu podklady k výrobě desky a krabičky z 3D tiskárny.

| Konstrukce | Jak funguje | Počet součástek | Pro nás |
| --- | --- | --- | --- |
| [Elektronická kostka](https://www.elektrokrouzek.cz/cs/clanky/2025-konstrukce-kostka) | Po stisku tlačítka čísla rychle běží, pípá, zpomaluje a zastaví se na 1–6. NE555 a čítač 4017, LED rozmístěné jako na kostce. | asi 30, obvody v paticích, LED srovnané podložkou | kandidát na závěrečnou výzvu (12) |
| [Useless box](https://www.elektrokrouzek.cz/cs/clanky/2025-useless-box) | Dva časovače NE555 řídí servo. Rameno vypne páčku a obvod se sám odpojí (MOSFET), takže nepotřebuje vypínač. Výchylky serva se nastavují trimry. | asi 20 a servo, nastavování je náročnější | spíš pro pokročilé; jako ukázka láká |
| [Bouřkoměr](https://www.elektrokrouzek.cz/cs/clanky/2025-bourkomer) | Start při blesku, stop při hromu; dva sloupce LED ukážou vzdálenost po 1 km a po 100 m. | přes 40, součástky z obou stran desky | moc náročné |

Další projekty na GitHubu: kuchyňská minutka z logických obvodů, hodiny z obvodů CMOS 4000, tester součástek s OLED displejem, LED budík, reakční hra a piškvorky s RP2040, 3D vánoční stromeček s tranzistory, Bluetooth reproduktor, Wi-Fi RGB lampa.

## Teorie pro děti

Články vysvětlují elektřinu stejným způsobem jako my: přes vodu, bez zbytečných vzorců. Ohmův zákon a výkon ale už počítají, to je pro starší děti.

- **Co je to elektřina:** podrobný postup pokusů s vodním modelem (viz výše).
- **Elektrické schéma:** schéma jako mezinárodní jazyk. Pěkný detail: tečka na křížení čar „je kapka cínu“, která vodiče spojuje, a vedle je to vidět na fotce skutečného spoje.
- **Kontaktní pole:** barevný obrázek, které díry jsou propojené (sloupce na napájení, řádky uprostřed). První zapojení: tlačítko, odpor a LED na 2× AA.
- **Kondenzátor:** dvě nádrže spojené hadicí; nabitý kondenzátor se dá odpojit a pak chvíli rozsvítí LED. Kondenzátor s malým povoleným napětím je jako malá nádrž, která přeteče.
- **Rezistor, trimr, potenciometr:** barevné proužky, trimr jako jezdec na dráze, rezistor se „potí“ (přeměňuje energii na teplo), rychlovarná konvice jako velký odpor.
- **Micropython a RP2040 Zero** v Thonny: návod na první program, pro starší děti.

## Vybavení podle nich

- **Pájecí stanice:** aspoň 40 W. Nejlepší je topné těleso přímo v hrotu; před koupí se podívat, kolik stojí náhradní hroty. Používají ATETOOL AE380 80 W (asi 1 400 Kč, bighobby.cz).
- **Cín:** bezolovnatý dělá začátečníkům potíže, hrot oxiduje a černá. Hrot čistit vlhkou houbičkou, drátěnka zkracuje jeho životnost a rychle čistí salmiak. Stanici vypínat, když se nepoužívá. Pod pájení dát podložku (sololit, překližka).
- **Nářadí:** kleště Proskit z GME (ploché, kombinačky, kulaté, štípací), odizolovací kleště, šroubováky, pinzeta, malý svěrák jako „třetí ruka“.
- **Součástky:** začínat jen s vývodovými (THT), roztříděnými do krabiček podle druhu. Sady rezistorů a kondenzátorů z GME, tranzistory a LED z Drátku, kontaktní pole ZY-204.
- **E-shopy, které uvádějí:** GME, TME, Tipa, Hadex, Drátek, Laskakit, Kondík, Půhy; dál Allegro, Farnell, Mouser a AliExpress.
