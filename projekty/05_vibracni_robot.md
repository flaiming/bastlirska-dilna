# 05 Vibrační robot z kartáče

**Stav:** návrh; motor vybrán a otestován (16. 10. 2026), zbývá ověřit oba druhy kartáčů  
**Pro koho:** 3.–5. třída; skupina A 9 dětí, skupina B 8 dětí, obvykle chybí 1–2  
**Délka:** přibližně 120 minut  
**Kdy:** 4. lekce každé skupiny, hned po drátěném hlavolamu (druhé pájení)  
**Co si děti odnesou:** vlastního robota **bez baterií** (motor, vypínač a držák jsou zapájené, jdou s ním). Baterie jsou dílenské a zůstávají; doma stačí vložit 2× AA.

## Cíl a princip

Dítě postaví robota z kartáče, motorku s excentrem a baterie. Excentr (závaží mimo osu) rozkmitá celý kartáč a šikmé štětiny převádějí kmitání na pohyb jedním směrem. Hlavní poznatek: **pohyb robota ovlivňuje, kde je motorek, jak velké je závaží a kam jsou skloněné štětiny**. Děti to ladí samy.

## Konstrukce

```
  držák 2× AA (+) ──── vypínač ──── motorek 130 ──── (−) držák
                                        │
                                   excentr na hřídeli
```

- **Kartáč:** 10× kartáč na boty (asi 15 × 5 × 4 cm, jemné štětiny) a 10× rýžák (větší, tuhé štětiny). V každé skupině půlka dětí s každým druhem, na konci srovnání.
- **Motorek:** [DC motor 3–5 V, 17–18 000 ot/min z Dratek.cz](https://dratek.cz/arduino-platforma/2987-dc-motor-3-5v-17-18000rpm.html) (hřídel 2 mm, tělo 20 × 27 mm, 25 Kč), přilepený nebo přichycený stahovací páskou u **jednoho konce** kartáče, hřídel přesahuje přes okraj.
- **Excentr:** 3D tištěný díl nalisovaný na hřídel ([model](../modely/excentr.scad)), v rameni zašroubovaný šroubek M3 jako závaží. Vyrábí vedoucí předem (viz příprava).
- **Místo pro excentr:** hřídel **nesmí přečnívat přes okraj kartáče**. Robot se pak při nárazu do překážky odrazí a excentr se o nic nezasekne (ověřeno na prototypu 16. 10. 2026). Motor proto leží na hřbetu kartáče na **podložce**, aby se šroubek točil volně nad kartáčem: hřídel musí být výš než poloměr otáčení šroubku. Podložka: špalík, kus korku nebo 2–3 slepená víčka; výšku podle vzorku.
- **Napájení:** držák 2× AA přilepený tavným lepidlem na hřbet kartáče. Pokud vzorek s rýžákem nepojede, zkusit 3× AA (4,5 V).
- **Vypínač:** malý kolébkový vypínač, přilepený navrch kartáče.
- **Zdobení:** děti robotovi dodělají oči, tykadla, ocásek. Není to jen ozdoba: každá přidaná věc mění rozložení váhy, a tím i směr jízdy (ověřeno na prototypu). Zdobení je proto součást ladění: „Přidej tykadlo vlevo, co se stane?“ Ozdoby nesmí zasahovat k excentru.

## Příprava vedoucího

1. **Vzorek s každým kartáčem.** Ověřit:
   - jestli rýžák pojede na 2× AA, nebo potřebuje 3× AA nebo větší excentr;
   - kam robot jede: kartáč na boty má rovné štětiny a může se jen točit; zkusit štětiny přejet do jedné strany nebo kartáč podložit, aby se naklonil;
   - kde má být motorek, aby kmitání bylo největší (obvykle na konci).
   Výsledek zapsat sem a podle něj objednat držáky.
2. **Excentry na všechny motorky** (3D tisk, model [`modely/excentr.scad`](../modely/excentr.scad), hotová STL vedle):
   - nejdřív vytisknout **zkušební destičku** (`excentr_zkouska.stl`, otvory 1,7–2,1 mm) a vybrat otvor, který jde na hřídel natlačit silou, ale bez praskání; hodnotu zapsat do `hridel_d` a vyexportovat excentr znovu;
   - tisknout naležato bez podpěr, PLA nebo PETG, 100% výplň (díl je malý, ať je těžký a pevný); 20 kusů najednou;
   - nalisovat na hřídel (podložit zadní konec hřídele, ne tlačit na motor), pro jistotu kapka vteřinového lepidla na rozhraní hřídele a náboje;
   - do ramene zašroubovat šroubek M3 o délce ověřené na vzorku (samořezně do plastu); **velikost excentru se ladí délkou šroubku a maticemi** navíc, což můžou zkoušet i děti;
   - poloměr otáčení je asi 9,5 mm od osy: motor na podložce tak, aby osa byla aspoň 11 mm nad hřbetem kartáče.
   Motor má 18 000 ot/min, takže excentr musí držet pevně: krátce roztočit a zkontrolovat, že nehází.
   Záloha bez tiskárny: šroubek přilepený tavným lepidlem napříč přes odmaštěnou a zdrsněnou hřídel.
3. Odizolovat konce vodičů držáků a připravit krátké kousky lanka (2× asi 10 cm na robota) od vypínače k motorku.
4. Pájecí stanoviště stejné jako u hlavolamu.

## Materiál a nákup

Počítáno na **18 robotů** (17 dětí + 1 rezerva).

| Položka | Na dítě | Celkem | Koupit / zajistit / skladem | Poznámka |
| --- | ---: | ---: | --- | --- |
| Kartáč na boty / rýžák | 1 | 10 + 10 | Skladem | |
| [DC motor 3–5 V, 18 000 ot/min (Dratek.cz)](https://dratek.cz/arduino-platforma/2987-dc-motor-3-5v-17-18000rpm.html) | 1 | 17 + 1 | Koupit | 25 Kč/ks; vzorek otestován, jede se šroubkem jako excentrem. |
| [Kolébkový vypínač 15 × 10,5 mm, Dratek](https://dratek.cz/arduino-platforma/7699-kolebkovy-vypinac-ac-3a-250v.html) | 1 | 17 + 1 | Koupit | 4,80 Kč od 10 ks. |
| [Držák 2× AA DPS DIL, Dratek](https://dratek.cz/arduino-platforma/122975-drzak-baterie-2x-aa-dps-dil.html) | 1 | 17 + 1 | Koupit | 12 Kč; děti pájí vodiče k vývodům. Baterie pojistit gumičkou, při vibracích můžou vyskočit. Alternativa: box s krytem a vypínačem (20 Kč), pak odpadá vypínač. |
| Baterie AA (dílenská sada) | 2 po dobu lekce | 13 párů | Skladem (16 alkalických + 10 nabíjecích), sdílená s hlavolamem | Zůstávají v dílně, děti si je neodnášejí. Při 3× AA o polovinu víc. |
| Šroubky různých velikostí | 1 | asi 25 | Skladem (krabička šroubků) | Na excentry; nekupovat. |
| Tištěný excentr ([model](../modely/excentr.scad)) | 1 | 17 + 3 | Vytisknout | Nalisovat na hřídel; nahrazuje pastorek z Techfunu. |
| Šroubky M3 různých délek + matice M3 | 1 + pár matic | asi 25 + 30 matic | Skladem (krabička šroubků), ověřit M3 | Závaží excentru; ladí se délkou a maticemi. |
| Tavné lepidlo | – | několik tyčinek | Skladem | Excentry dělá vedoucí předem; motor, podložku, držák, vypínač a ozdoby lepí děti. |
| Stahovací pásky | 1–2 | 1 balení | Koupit / skladem | Pojistka motorku. |
| Lanko | 20 cm | asi 4 m | Skladem | |
| Plastelína | kousek | – | Skladem | Ladění: přidávání závaží na kartáč (ne na hřídel). |
| Pohyblivá očička | 2 | asi 50 | Koupit (papírnictví, hobby) | Zdobení; samolepicí, nebo lepit tavnou pistolí. |
| Velké sponky, chlupaté (plyšové) drátky | 2–3 | – | Sponky skladem, drátky koupit | Tykadla, nožičky, ocásek; zároveň závaží na ladění. |

**Vratné vybavení:** pájky, kleště, odizolovací kleště, multimetr, svinovací metr nebo pásky na podlaze jako dráha.

## Postup lekce

| Čas | Co dělají děti a vedoucí |
| --- | --- |
| 0–10 min | Ukázka vzorku. Proč se kartáč hýbe? Motorek bez excentru vs. s excentrem v ruce: cítit kmitání. Připomenout pravidla pájení. |
| 10–70 min | **Stanoviště** (2 rotace po ~30 min): ① **pájení u vedoucího:** vodiče držáku a lanka k vypínači a k motorku (4 spoje) · ② **příprava kartáče:** vybrat druh kartáče a excentr, rozmyslet umístění, přilepit držák a vypínač. Kdo čeká, jde k Voltíkovi. |
| 70–80 min | Kompletace: přichytit motorek (tavná pistole, případně pojistit stahovací páskou), první jízda. |
| 80–105 min | **Zdobení, ladění a závody:** oči, tykadla a ocásek; pozorovat, jak ozdoby mění jízdu. Změnit jednu věc (poloha motorku, velikost excentru, ozdoba nebo plastelína na jedné straně) a porovnat. Závod rovně, závod v kruhu, srovnání kartáč na boty vs. rýžák. |
| 105–120 min | Úklid, co pomohlo robotovi jet rovně. **Vyndat baterie** zpět do dílenské krabičky (vedoucí počítá páry), robot jde domů prázdný se štítkem „doma vložit 2× AA“. |

## Tipy při stavbě a když to nefunguje

- **Motorek se netočí:** vypínač zapojený mimo obvod (oba vodiče na stejné očko), studený spoj, vybité baterie. Zkusit motorek napřímo na baterii.
- **Točí se, ale robot stojí:** malý excentr nebo těžký kartáč; dát velký excentr, zkusit 3× AA, motorek blíž ke konci.
- **Robot se jen točí dokola:** štětiny jsou rovné nebo motorek je na boku; posunout motorek na osu kartáče, naklonit štětiny, přidat plastelínu na druhou stranu.
- **Robot jede pozpátku nebo bokem:** otočit motorek nebo přehodit vodiče u motorku (změna směru otáčení).
- **Excentr tluče do kartáče nebo do ozdob:** motor víc podložit, ozdoby dát dál od hřídele.
- **Excentr odletěl:** víc lepidla kolem hřídele, nechat vychladnout. Plastelínu na hřídel nedávat.
- **Snazší varianta:** vedoucí předpájí vodiče k motorku; dítě pájí jen vypínač.
- **Rozšíření:** na kartáč připevnit fixy jako nožky a robot kreslí po papíře; nebo postavit „arénu“ a hrát robotí fotbal s pingpongovým míčkem.

## Kreslící varianta z kelímku

Skladem je 30 kelímků. Kelímek se otočí dnem vzhůru, kolem okraje se izolepou připevní 3–4 fixy hroty dolů jako nožičky (víčka sundaná, izolepu ne tavné lepidlo, aby šly fixy vyndat). Na dno kelímku se přilepí motor s excentrem a držák baterií. Robot se postaví na velký papír (balicí papír, role) a kreslí čmáranice; podle polohy motoru a počtu nožiček kreslí kruhy, smyčky nebo jezdí rovně.

Možnosti zařazení:
- **Výběr v lekci 4:** každé dítě si vybere kartáč, nebo kelímek. Stejný motor, držák i pájení, nic navíc se nekupuje.
- **Samostatná lekce „Vibrobot II“:** děti si postaví druhého robota úplně samy (opakování pájení bez pomoci). Potřeba další sada motor + držák + vypínač, orientačně 850 Kč na 20 robotů; baterie z dílenské sady.
- **Rozšíření pro rychlé děti v lekci 4:** 2–3 kelímkové roboty z rezervních motorů.

Fixy: vypratelné, 3–4 na robota (asi 60–80 ks na skupinu, nebo děti přinesou vlastní). Papír chránit podložkou, fixy prosakují.

## Bezpečnost

Excentr se točí rychle a je zvenku přístupný: dlouhé vlasy svázat, prsty mimo, před manipulací robota vypnout. Zablokovaný motorek se zahřívá, takže vypnout. Pájení stejně jako u hlavolamu (pájka ve stojánku, brýle, větrání, umýt ruce). Tavné pistole: děti lepí samy (ze školy jsou zvyklé), ale jen u horkého stolu vedle vedoucího; pistole vždy zpět do stojánku, nesahat na trysku ani na čerstvé lepidlo, při popálení chladit pod studenou tekoucí vodou. Baterie nezkratovat.

## Inspirace a zdroje

Kartáčový robot (bristlebot) ve větším provedení s motorkem typu 130. Motorek typu 130 má podle prodejců hřídel 2 mm a pracuje na 3–6 V ([Little Bird](https://littlebirdelectronics.com.au/products/130-size-hobby-motor-3-6v-4000rpm.json)). Hotové vibrační motorky 130 s excentrem z výroby existují také, ale vlastní excentr z tavného lepidla a šroubku je levnější a dá se upravit.

## Po lekci

- **Prototyp (16. 10. 2026):** kompletní robot funguje. Lepší, když hřídel nepřečnívá (robot se odrazí od překážky). Ozdoby na stranách mění jízdu.
- **Vzorek (16. 10. 2026):** motor z Dratek.cz jede, když je na hřídeli „tak akorát“ velký šroubek; malý excentr nestačí. Doplnit přesnou velikost šroubku.
- **Vzorek před lekcí:** který kartáč jel lépe, 2× nebo 3× AA, malý nebo velký excentr, nejlepší poloha motorku.
- **Skupina A:** kolik zabralo pájení, co se nejčastěji kazilo, výsledky závodů.
- **Skupina B:** finální úpravy a spotřeba.
