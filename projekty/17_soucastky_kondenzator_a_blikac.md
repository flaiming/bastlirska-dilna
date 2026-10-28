# 17 Objevujeme součástky III: kondenzátor a blikač

**Stav:** osnova; zapojení ověřit na vzorku (3 V)  
**Pro koho:** 3.–5. třída; skupina A 9 dětí, skupina B 8 dětí, obvykle chybí 1–2  
**Délka:** přibližně 120 minut  
**Kdy:** po lekci 16 (tranzistor)  
**Co si děti odnesou:** nic; blikač si postaví na kontaktním poli. Domů si ho odnesou až z lekce 18 (vlastní plošný spoj), kde se z něj stane výrobek.

## Cíl a princip

- **Kondenzátor je kyblík na elektřinu.** Nabije se z baterie a pak chvíli sám napájí LED. Větší kondenzátor = větší kyblík = LED svítí déle.
- **Blikač** ze dvou tranzistorů a dvou kondenzátorů: kondenzátory se střídavě nabíjejí a vybíjejí a přepínají tranzistory. Děti mění kondenzátor nebo odpor a sledují, jak se mění rychlost blikání.

Proč blikač nepájet už tady: má asi 20 spojů. S devíti dětmi a dvěma páječkami by pájení zabralo víc než celou lekci; na kontaktním poli ho dvojice postaví za 20–30 minut.

## Funkční varianta a příprava vedoucího

- **Kyblík:** elektrolytický kondenzátor 1000–2200 µF nabít dotykem na 2× AA, pak připojit k LED s odporem 1 kΩ. LED pomalu zhasíná. Porovnat 100 µF a 2200 µF.
- **Schodišťové světlo:** tlačítko nabije kondenzátor, ten přes odpor drží otevřený tranzistor a LED po puštění tlačítka ještě několik sekund svítí a pomalu zhasne.
- **Blikač (astabilní klopný obvod) na 3 V:** dva NPN tranzistory, dvě LED s odpory asi 220–470 Ω v kolektorech, odpory do bází asi 47 kΩ, kondenzátory 10–47 µF. S 47 kΩ a 22 µF bliká zhruba jednou za sekundu. Hodnoty ověřit na vzorku.

Příprava:

1. Postavit všechna tři zapojení na 3 V a vybrat hodnoty, které fungují s tranzistory ze skladu.
2. Kartičky zapojení 1 : 1 (jako v lekci 16); u blikače postup po krocích: nejdřív jedna polovina, vyzkoušet, pak druhá.
3. Při ladění vzorků napájet z laboratorního zdroje (3 V, omezení proudu asi 100 mA): špatně otočený tranzistor nebo zkrat se projeví poklesem napětí, nic se nespálí.
4. Upozornit: elektrolytický kondenzátor má plus a mínus (proužek je mínus); vedoucí kontroluje před připojením baterie.

## Materiál a nákup

Vratné, pro 4–5 dvojic:

| Položka | Celkem | Koupit / zajistit / skladem | Poznámka |
| --- | ---: | --- | --- |
| Elektrolytické kondenzátory 10, 22, 47, 100, 1000, 2200 µF (do 16–25 V) | po 5–10 | Skladem, doplnit sadou | Sadu elektrolytů koupit u českého prodejce. |
| NPN tranzistory | 10–15 | Skladem | Stejné jako v lekci 16. |
| Tlačítka do kontaktního pole | 5 | Skladem | |
| LED, odpory 220 Ω, 1 kΩ, 10 kΩ, 47 kΩ | po 10 | Skladem | |
| Kontaktní pole, propojky, držáky 2× AA | 5 | Z lekce 16 | |

## Postup lekce (osnova)

| Čas | Co dělají děti a vedoucí |
| --- | --- |
| 0–10 min | Pas součástek: co už známe. Nová tajemná součástka: kondenzátor. |
| 10–35 min | Dvojice: kyblík (malý vs. velký kondenzátor), měřit, jak dlouho LED dosvítí (stopky v mobilu). |
| 35–55 min | Schodišťové světlo s tranzistorem. |
| 55–100 min | Blikač po krocích; kdo má hotovo, mění kondenzátory a soutěží, kdo má nejpomalejší a nejrychlejší blikání. |
| 100–120 min | Ukázka: z tohoto zapojení si v lekci 18 vyrobíme vlastní plošný spoj. Pas součástek, úklid. |

## Bezpečnost

Jen bateriové napětí. Elektrolytický kondenzátor zapojený obráceně se může nafouknout nebo prasknout; na 3 V je to nepravděpodobné, ale pravidlo „proužek k mínusu, vedoucí zkontroluje“ platí vždy. Nikdy nepoužívat kondenzátory vymontované ze starých spotřebičů (mohou být nabité).

## Po lekci

- **Vzorek:** hodnoty odporů a kondenzátorů blikače, které spolehlivě fungují na 3 V.
- **Skupina A:** kolik dvojic dostalo blikač do chodu? Kde se nejčastěji chybovalo?
- **Skupina B:** úpravy.
