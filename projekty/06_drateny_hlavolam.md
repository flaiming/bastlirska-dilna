# 06 Drátěný hlavolam s bzučákem (Elektrická dílna I)

**Stav:** návrh; před nákupem postavit jeden vzorek a ověřit bzučák na 3 V  
**Pro koho:** 3.–5. třída; skupina A 9 dětí, skupina B 8 dětí, obvykle chybí 1–2  
**Délka:** přibližně 120 minut  
**Kdy:** 3. lekce každé skupiny, první lekce s pájením  
**Co si děti odnesou:** vlastní hlavolam **bez baterií** (bzučák a držák jsou zapájené, jdou s ním). Baterie jsou dílenské a zůstávají; doma stačí vložit 2× AA.

## Cíl a princip

Dítě postaví hlavolam: vede drátěné očko po zprohýbané drátěné dráze a nesmí se jí dotknout. Při dotyku se uzavře obvod a bzučák pípne. Hlavní poznatek: **obvod funguje, jen když je uzavřený**. Hlavolam je spínač, který se sepne omylem.

Zároveň je to první pájení. Každé dítě zapájí spoje na **vlastním** výrobku, takže pájení není jen cvičení.

## Úvod přes sponkový vypínač

Na začátku vedoucí ukáže na sponkovém vypínači uzavřený a rozpojený obvod ([nákres a schéma](https://claude.ai/artifact/VuQKH2Ey1gEcUX36jZB9fk)). Stačí jeden předem postavený kus: baterie → bzučák → sponkový vypínač. Pak se zeptat: „Jak udělat spínač, který sepneš, když se netrefíš?“

## Konstrukce

```
          bzučák
   (+)  ┌──[ B ]──┐  (−)
        │         │
  držák 2× AA     └──── drát ──── konec dráhy (pod podstavcem)
        │
   (−)  └──── ohebné lanko 40 cm ──── očko na rukojeti
```

- **Podstavec:** prkýnko přibližně 25 × 8 cm (skladem) se dvěma předvrtanými otvory asi 20 cm od sebe. Konec dráhy se zastrčí do otvoru a u jednoho konce se k prkýnku **přišroubuje** vrutem s podložkou spolu s odizolovaným koncem lanka od bzučáku. To je zároveň elektrický spoj, takže funguje i s pozinkovaným drátem.
- **Dráha:** holý drát 1,5–2 mm, asi 60 cm: měděný, nebo pozinkovaný (zkouší se, zda jde pájet). Pozinkovaný drát s kalafunou obvykle pájet nejde; pak drát k dráze **nepájet, ale přichytit šroubkem s podložkou** do podstavce (konec dráhy i odizolované lanko pod hlavičku šroubku). Kyselou pájecí vodu na to nepoužívat. Děti ho zprohýbají do vln a smyček, konce se zastrčí do otvorů a zajistí tavným lepidlem.
- **Odkládací místa:** oba konce dráhy omotat asi 3 cm izolepy. Tam se očko odkládá na startu a v cíli a nepípá.
- **Očko:** měděný drát asi 20 cm; na konci ohnout očko o průměru 1,5–2 cm, zbytek je rukojeť omotaná izolepou. Očko nechat s **malou mezerou** (háček), aby se dalo nasadit na hotovou dráhu. Uzavřené očko se musí navléknout dřív, než se zalepí druhý konec dráhy.
- **Elektrika:** plus baterie → bzučák → drát ke konci dráhy. Mínus baterie → dlouhé ohebné lanko → očko. Dotyk očka s dráhou obvod uzavře.

**Záložní bzučák:** Voltík I a II mají každý svůj bzučák. Na zkoušení hlavolamů v lekci stačí, ale domů si pak děti hlavolam bez bzučáku odnesou. Proto bzučák za 5 Kč koupit a Voltíka nechat jako zálohu.

## Příprava vedoucího

1. Postavit vzorek. Ověřit, že bzučák pípá na 2 tužkové baterie dost nahlas a že cín drží na zvoleném drátu.
2. Nařezat a předvrtat podstavce. Průměr otvoru podle drátu, aby drát šel zasunout těsně.
3. Nastříhat dráty na dráhu (60 cm) a očko (20 cm) a lanka (40 cm). Konce lanek a vodičů odizolovat asi 1 cm.
4. Pájecí stanoviště: stojánek, mosazná drátěnka na hrot (mokrá houbička jen záloha, hrotu škodí teplotní šok), silikonová pájecí podložka (4 ks, ne papír ani karton), brýle pro zájemce, „třetí ruka“ nebo kolíček, cín s kalafunou, větrání. Mikropájku pro děti, trafopájku jen vedoucí.
5. Kartička pro Voltíka: vybrat 3–4 pokusy, ideálně se spínačem, LED nebo bzučákem.
6. Postavit ukázkový sponkový vypínač s bzučákem.
7. **Zkoušky na laboratorním zdroji** (omezení proudu asi 200 mA): jak hlasitě bzučák pípá na 2,4 V (nabíjecí baterie) a na 3 V; při jakém napětí sepne relé SRD-05VDC na bonus (od 2 V pomalu přidávat do cvaknutí). Sepne-li až nad asi 2,8 V, bonus napájet ze 3× AA a ověřit, že bzučák 4,5 V snese. Zdroj se hodí i na zkoušení hotových hlavolamů místo baterií.

## Materiál a nákup

Počítáno na **20 hlavolamů** (17 dětí + rezerva).

| Položka | Na dítě | Celkem | Koupit / zajistit / skladem | Poznámka |
| --- | ---: | ---: | --- | --- |
| [Aktivní bzučák 3,3 V, Laskakit](https://www.laskakit.cz/aktivni-bzucak-3-3v-5v/?variantId=22805) | 1 | 17 + 1 | Koupit | 6 Kč, varianta LA216000A na 3,3 V; na 2× AA pípá naplno. Delší vývod je plus. |
| [Držák 2× AA DPS DIL, Dratek](https://dratek.cz/arduino-platforma/122975-drzak-baterie-2x-aa-dps-dil.html) | 1 | 17 + 1 | Koupit | 12 Kč. Bez drátů: děti připájí vodiče k vývodům. Vypínač není potřeba. |
| Baterie AA (dílenská sada) | 2 po dobu lekce | 13 párů | Skladem (16 alkalických + 10 nabíjecích), sdílená s vibrobotem | Zůstávají v dílně, děti si je neodnášejí. |
| Holý měděný drát 1,5–2 mm | 80 cm | asi 16 m | Zkontrolovat krabici drátů, jinak koupit | Na dráhu a očko; ne pozinkovaný ani ocelový (cín by nedržel). |
| Ohebné lanko | 50 cm | asi 10 m | Skladem (krabice drátů) | K očku a od bzučáku k dráze. |
| Prkýnko asi 25 × 8 cm | 1 | 20 | Skladem | Konce dráhy a lanka se přišroubují. |
| Vruty do dřeva s podložkou | 2 | asi 45 | Skladem (krabička šroubků) | Stažení konce dráhy a lanka k prkýnku. |
| Izolepa | kousky | 1–2 role | Skladem / koupit | Konce dráhy, rukojeť, izolace spojů. |
| Cín s kalafunou | – | – | Skladem | |
| Tavné lepidlo | – | několik tyčinek | Skladem | Zajištění dráhy v podstavci; lepí děti u horkého stolu. |

**Vratné vybavení:** mikropájka a trafopájka se stojánky, kleště a štípačky (2–3 sady), odizolovací kleště, multimetr na hledání chyb, Voltík I a II.

## Postup lekce

Při 7–8 dětech 3 skupinky po 2–3; vedoucí sedí u pájení.

| Čas | Co dělají děti a vedoucí |
| --- | --- |
| 0–15 min | **Všichni:** ukázka sponkového vypínače s bzučákem. Ukázka pájení a pravidla: pájka vždy ve stojánku, nesahat na hrot ani na čerstvý spoj, pájet jen u stolu s vedoucím, po pájení umýt ruce. |
| 15–43 min | **Rotace 1** |
| 43–71 min | **Rotace 2** |
| 71–99 min | **Rotace 3** |
| 99–112 min | **Kompletace:** dráha do podstavce (děti zalepí tavnou pistolí, vedoucí hlídá), drát od bzučáku omotat kolem konce dráhy pod podstavcem, nasadit očko, vyzkoušet. |
| 112–120 min | Kdo projde dráhu bez pípnutí? **Vyndat baterie** zpět do dílenské krabičky, hlavolam jde domů se štítkem „doma vložit 2× AA“. Úklid. |

**Stanoviště:**

- **① Pájení (s vedoucím):** rozcvička, tj. pocínovat a spojit dva kousky drátu (asi 3 min). Pak spoje na vlastním hlavolamu: plus držáku k bzučáku, bzučák k drátu ke dráze, lanko k očku. Spoje omotat izolepou. Každé dítě si spoje podepíše na papírový štítek.
- **② Stavba hlavolamu:** ohnout dráhu (nejdřív vymyslet tvar, pak ohýbat kleštěmi i rukama), omotat konce izolepou, ohnout očko s rukojetí. Mírně obtížnější dráha = víc zábavy, ale očko musí projít všemi zatáčkami.
- **③ Voltík I nebo II:** pokusy podle kartičky. Kdo je hotový, zkusí změnit jednu věc a zjistit, co se stane.

## Tipy při stavbě a když to nefunguje

- **Nepípá ani při dotyku:** zkontrolovat polaritu bzučáku (plus k plusu baterie), zda je bzučák aktivní, a zda spoj drátu s dráhou není pod lakem nebo izolepou. Multimetrem změřit průchodnost.
- **Pípá pořád:** očko leží na holé dráze, nebo se lanko holým koncem dotýká dráhy či baterie.
- **Cín nedrží:** drát je zoxidovaný (zbrousit smirkem), pájka je studená, nebo jde o ocelový drát.
- **Očko neprojde zatáčkou:** zvětšit očko nebo dráhu v ostrých místech rozevřít.
- **Snazší varianta:** vedoucí připraví dráhu předem ohnutou; dítě jen pájí a sestavuje.
- **Rozšíření:** přidat LED s rezistorem paralelně k bzučáku; nebo udělat dráhu ve dvou úrovních.
- **Bonus pro rychlé: hlavolam s pamětí.** Samodržné relé SRD-05VDC (objednáno 6 ks; cívka 5 V, sepnutí na 3 V ověřit na zdroji, jinak napájet 4,5 V: k držáku 2× AA přidat do série držák 1× AA): kontakt COM–NO paralelně k očku a dráze, cívka a bzučák za nimi, vypínač v přívodu jako reset, dioda 1N4007 přes cívku. Jen pár kusů relé, ne pro všechny; zapojuje se krokosvorkami a relé zůstává v dílně. Cívka bere asi 100 mA, po hře vypnout. Před lekcí vyzkoušet. [Interaktivní schéma](https://claude.ai/artifact/148C6rAzAbfM6g89yegQUa).

## Bezpečnost

Pájka: hrot má přes 300 °C; pájka vždy ve stojánku, kabel mimo dosah rukou, pod spoj podložka. Děti pájí jen u stolu s vedoucím. Brýle doporučit, ale nevyžadovat; hlavně při štípání drátu, kdy odštípnutý konec může odletět (konec přidržet, mířit dolů). Kalafuna kouří: větrat, nedýchat přímo nad spojem. Po pájení umýt ruce. Při popálení chladit pod tekoucí studenou vodou. Trafopájka jen vedoucí. Tavné pistole: děti lepí samy (ze školy jsou zvyklé), ale jen u horkého stolu vedle vedoucího; pistole vždy zpět do stojánku, nesahat na trysku ani na čerstvé lepidlo, při popálení chladit pod studenou tekoucí vodou. Konce drátů jsou ostré: zastřihnout a ohnout dovnitř. Baterie nezkratovat: držák nikdy nespojit napřímo bez bzučáku.

## Inspirace a zdroje

Klasický „drátěný hlavolam“ (buzz wire game). Úvodní ukázka používá [nákres sponkového vypínače](https://claude.ai/artifact/VuQKH2Ey1gEcUX36jZB9fk).

## Po lekci

- **Vzorek před lekcí:** doplnit použitý drát, typ bzučáku a hlasitost na 3 V.
- **Skupina A:** stihla se rotace? Kolik minut pájení vyšlo na dítě? Kolik spojů se muselo opravovat? Stačila 2 pájecí místa pro děti (PLSD 60 C3 + mikropájka), nebo dokoupit druhou PLSD?
- **Skupina B:** finální úpravy a spotřeba materiálu.
