# 05 Vibrační robot z kartáče

**Stav:** návrh; motor vybrán a otestován (16. 10. 2026), zbývá ověřit oba druhy kartáčů  
**Pro koho:** 3.–5. třída; skupina A 9 dětí, skupina B 8 dětí, obvykle chybí 1–2  
**Délka:** přibližně 120 minut  
**Kdy:** 4. lekce každé skupiny, hned po drátěném hlavolamu (druhé pájení)  
**Co si děti odnesou:** vlastního robota

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
- **Excentr:** vlastní výroba vedoucím (viz příprava), šroubek přilepený na hřídel.
- **Místo pro excentr:** hřídel **nesmí přečnívat přes okraj kartáče**. Robot se pak při nárazu do překážky odrazí a excentr se o nic nezasekne (ověřeno na prototypu 16. 10. 2026). Motor proto leží na hřbetu kartáče na **podložce**, aby se šroubek točil volně nad kartáčem: hřídel musí být výš než poloměr otáčení šroubku. Podložka: špalík, kus korku, 2–3 slepená víčka nebo vrstvená pěnová páska; výšku podle vzorku.
- **Napájení:** držák 2× AA na hřbetu kartáče (oboustranná pěnová páska). Pokud vzorek s rýžákem nepojede, zkusit 3× AA (4,5 V).
- **Vypínač:** malý kolébkový vypínač, přilepený navrch kartáče.
- **Zdobení:** děti robotovi dodělají oči, tykadla, ocásek. Není to jen ozdoba: každá přidaná věc mění rozložení váhy, a tím i směr jízdy (ověřeno na prototypu). Zdobení je proto součást ladění: „Přidej tykadlo vlevo, co se stane?“ Ozdoby nesmí zasahovat k excentru.

## Příprava vedoucího

1. **Vzorek s každým kartáčem.** Ověřit:
   - jestli rýžák pojede na 2× AA, nebo potřebuje 3× AA nebo větší excentr;
   - kam robot jede: kartáč na boty má rovné štětiny a může se jen točit; zkusit štětiny přejet do jedné strany nebo kartáč podložit, aby se naklonil;
   - kde má být motorek, aby kmitání bylo největší (obvykle na konci).
   Výsledek zapsat sem a podle něj objednat držáky.
2. **Excentry na všechny motorky** (den předem, ať lepidlo vychladne):
   - šroubek o velikosti ověřené na vzorku, přilepený tavným lepidlem napříč přes hřídel tak, aby přečníval na jednu stranu;
   - z krabičky šroubků vybrat několik velikostí kolem té ze vzorku a motory s nimi rozdělit, aby děti mohly porovnávat; motory označit podle velikosti šroubku.
   Motor má 18 000 ot/min, takže závaží musí držet opravdu pevně.
   Lepší držení: nejdřív na hřídel nalisovat plastový pastorek ([Techfun, 9 zubů, otvor 1,9 mm](https://techfun.cz/produkt/ozubene-kolecko-pro-dc-motorky-9-zubu/), 5 Kč) a šroubek lepit na něj. Bez pastorku hřídel odmastit a zdrsnit smirkem, případně omotat několika závity tenkého drátu nebo navléknout kousek izolace z drátu.
   Lepidlo musí obalit hřídel i závaží; nechat úplně vychladnout a zkusit krátce roztočit. Polovinu motorků s kratším, polovinu s delším šroubkem.
3. Odizolovat konce vodičů držáků a připravit krátké kousky lanka (2× asi 10 cm na robota) od vypínače k motorku.
4. Pájecí stanoviště stejné jako u hlavolamu.

## Materiál a nákup

Počítáno na **20 robotů** (17 dětí + rezerva).

| Položka | Na dítě | Celkem | Koupit / zajistit / skladem | Poznámka |
| --- | ---: | ---: | --- | --- |
| Kartáč na boty / rýžák | 1 | 10 + 10 | Skladem | |
| [DC motor 3–5 V, 18 000 ot/min (Dratek.cz)](https://dratek.cz/arduino-platforma/2987-dc-motor-3-5v-17-18000rpm.html) | 1 | 20 + 2 | Koupit | 25 Kč/ks; vzorek otestován, jede se šroubkem jako excentrem. |
| [Kolébkový vypínač 15 × 10,5 mm, Dratek](https://dratek.cz/arduino-platforma/7699-kolebkovy-vypinac-ac-3a-250v.html) | 1 | 20 + 2 | Koupit | 4,80 Kč od 10 ks. |
| [Držák 2× AA DPS DIL, Dratek](https://dratek.cz/arduino-platforma/122975-drzak-baterie-2x-aa-dps-dil.html) | 1 | 20 | Koupit | 12 Kč; děti pájí vodiče k vývodům. Baterie pojistit gumičkou, při vibracích můžou vyskočit. Alternativa: box s krytem a vypínačem (20 Kč), pak odpadá vypínač. |
| Baterie AA | 2 | 40 + rezerva | Koupit | Při 3× AA o polovinu víc. |
| Šroubky různých velikostí | 1 | asi 25 | Skladem (krabička šroubků) | Na excentry; nekupovat. |
| [Pastorek 9 zubů, otvor 1,9 mm (Techfun)](https://techfun.cz/produkt/ozubene-kolecko-pro-dc-motorky-9-zubu/) | 1 | 22 + pár navíc | Koupit | 5 Kč/ks; nalisovat na hřídel, šroubek lepit na něj. |
| Tavné lepidlo | – | několik tyčinek | Skladem | Excentry a motorek; obsluhuje vedoucí. |
| Oboustranná pěnová páska | kousek | 1 role | Koupit | Držák a vypínač na kartáč. |
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
| 70–80 min | Kompletace: přichytit motorek (stahovací páska + vedoucí zajistí tavnou pistolí), první jízda. |
| 80–105 min | **Zdobení, ladění a závody:** oči, tykadla a ocásek; pozorovat, jak ozdoby mění jízdu. Změnit jednu věc (poloha motorku, velikost excentru, ozdoba nebo plastelína na jedné straně) a porovnat. Závod rovně, závod v kruhu, srovnání kartáč na boty vs. rýžák. |
| 105–120 min | Úklid, co pomohlo robotovi jet rovně. |

## Tipy při stavbě a když to nefunguje

- **Motorek se netočí:** vypínač zapojený mimo obvod (oba vodiče na stejné očko), studený spoj, vybité baterie. Zkusit motorek napřímo na baterii.
- **Točí se, ale robot stojí:** malý excentr nebo těžký kartáč; dát velký excentr, zkusit 3× AA, motorek blíž ke konci.
- **Robot se jen točí dokola:** štětiny jsou rovné nebo motorek je na boku; posunout motorek na osu kartáče, naklonit štětiny, přidat plastelínu na druhou stranu.
- **Robot jede pozpátku nebo bokem:** otočit motorek nebo přehodit vodiče u motorku (změna směru otáčení).
- **Excentr tluče do kartáče nebo do ozdob:** motor víc podložit, ozdoby dát dál od hřídele.
- **Excentr odletěl:** víc lepidla kolem hřídele, nechat vychladnout. Plastelínu na hřídel nedávat.
- **Snazší varianta:** vedoucí předpájí vodiče k motorku; dítě pájí jen vypínač.
- **Rozšíření:** na kartáč připevnit fixy jako nožky a robot kreslí po papíře; nebo postavit „arénu“ a hrát robotí fotbal s pingpongovým míčkem.

## Bezpečnost

Excentr se točí rychle a je zvenku přístupný: dlouhé vlasy svázat, prsty mimo, před manipulací robota vypnout. Zablokovaný motorek se zahřívá, takže vypnout. Pájení stejně jako u hlavolamu (pájka ve stojánku, brýle, větrání, umýt ruce). Tavnou pistoli obsluhuje vedoucí. Baterie nezkratovat.

## Inspirace a zdroje

Kartáčový robot (bristlebot) ve větším provedení s motorkem typu 130. Motorek typu 130 má podle prodejců hřídel 2 mm a pracuje na 3–6 V ([Little Bird](https://littlebirdelectronics.com.au/products/130-size-hobby-motor-3-6v-4000rpm.json)). Hotové vibrační motorky 130 s excentrem z výroby existují také, ale vlastní excentr z tavného lepidla a šroubku je levnější a dá se upravit.

## Po lekci

- **Prototyp (16. 10. 2026):** kompletní robot funguje. Lepší, když hřídel nepřečnívá (robot se odrazí od překážky). Ozdoby na stranách mění jízdu.
- **Vzorek (16. 10. 2026):** motor z Dratek.cz jede, když je na hřídeli „tak akorát“ velký šroubek; malý excentr nestačí. Doplnit přesnou velikost šroubku.
- **Vzorek před lekcí:** který kartáč jel lépe, 2× nebo 3× AA, malý nebo velký excentr, nejlepší poloha motorku.
- **Skupina A:** kolik zabralo pájení, co se nejčastěji kazilo, výsledky závodů.
- **Skupina B:** finální úpravy a spotřeba.
