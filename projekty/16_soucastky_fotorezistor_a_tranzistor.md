# 16 Objevujeme součástky II: fotorezistor a tranzistor (světlo na tmu)

**Stav:** osnova; zapojení ověřit na vzorku (3 V, typ tranzistorů ve skladu)  
**Pro koho:** 3.–5. třída; skupina A 9 dětí, skupina B 8 dětí, obvykle chybí 1–2  
**Délka:** přibližně 120 minut  
**Kdy:** po lekci 15 (LED a odpor); obsahuje téma 09 „Světlo reagující na tmu“  
**Co si děti odnesou:** zatím nic, nebo noční světýlko (rozhodnout po vzorku, viz níže). Kontaktní pole a součástky na zkoušení zůstávají.

## Cíl a princip

- **Fotorezistor je odpor, který řídí světlo.** Na světle má malý odpor, ve tmě velký. Děti to změří multimetrem (zakrýt dlaní, posvítit mobilem).
- **Trimr je odpor s knoflíkem.** Otáčením se mění jas LED.
- **Tranzistor je elektrický kohoutek.** Malý proud do prostřední nožičky otevře velký proud pro LED. Díky němu jde obvod „obrátit“: LED se rozsvítí, když je tma.

Zlatý okamžik lekce: **dotykový spínač**. Dva tranzistory za sebou a prst mezi dvěma drátky rozsvítí LED. Děti zjistí, že jimi teče proud (velmi malý a bezpečný).

## Funkční varianta a příprava vedoucího

- **Poprvé kontaktní pole** ve dvojicích. Aby se děti neztrácely: malé pole (170 nebo 400 bodů), **kartičky se zapojením 1 : 1** (fotka nebo kresba pole se součástkami, přiložit a obkreslit), předem nastříhané propojky v barvách (červená plus, černá mínus), vedoucí zkontroluje zapojení, než se připojí baterie.
- **Světlo na tmu (3 V):** trimr 100 kΩ (nebo odpor 47 kΩ) z plusu do báze, fotorezistor z báze do mínusu, LED s odporem 100 Ω v kolektoru NPN tranzistoru. Na světle má fotorezistor malý odpor a stáhne bázi dolů, LED nesvítí; ve tmě LED svítí. Trimrem se nastaví, jak velká tma stačí.
- **Dotykový spínač:** dva NPN tranzistory v Darlingtonově zapojení, LED s odporem v kolektoru; na 3 V svítí slabě, na 3× AA (4,5 V) jasně. Ověřit na vzorku.

Příprava:

1. Zjistit typ tranzistorů ve skladu (BC547, 2N3904 a podobné NPN jsou vhodné) a fotorezistorů; postavit obě zapojení na 3 V.
2. Kartičky zapojení 1 : 1 pro: ① LED + trimr, ② fotorezistor + LED (svítí víc na světle, „obráceně, než chceme“), ③ světlo na tmu s tranzistorem, ④ dotykový spínač.
3. **Výrobek domů, rozhodnout po vzorku:** buď noční světýlko zapájené na kousek univerzálního pájivého pole podle předkreslené šablony (asi 8 spojů, držák 2× AA, baterie doma), nebo bez výrobku a světýlko si udělají až v lekci 18 na vlastním plošném spoji.

## Materiál a nákup

Vratné, pro 4–5 dvojic (nic z toho nejde domů, pokud se nedělá výrobek):

| Položka | Celkem | Koupit / zajistit / skladem | Poznámka |
| --- | ---: | --- | --- |
| Kontaktní pole 170 nebo 400 bodů | 5 | Doplnit; skladem „několik“ | Malá pole koupit u českého prodejce (Drátek, Laskakit). |
| Propojky do kontaktního pole | sada pro 5 míst | Skladem (Dupont) / doplnit | Pevné propojky jsou pro děti lepší než Dupont kabely. |
| NPN tranzistory | 10–15 | Skladem, ověřit typ | |
| Fotorezistory | 5–10 | Skladem | |
| Potenciometry RV09 s hřídelí a knoflíkem: 1 kΩ a 100 kΩ | po 5 | Koupit (Drátek, Laskakit, GME; AliExpress jen když tu nejsou) | 1 kΩ na stmívání LED, **vždy s pevným odporem 100 Ω v sérii** (na nule by LED neměla ochranu); 100 kΩ na nastavení světla na tmu. Hřídel s knoflíkem je pro děti lepší než trimr na šroubovák. |
| LED, odpory 100 Ω, 1 kΩ, 47 kΩ | po 10 | Skladem | |
| Držák 2× AA, případně 3× AA pro dotykový spínač | 5 | Dílenská sada | |

Spotřební jen při výrobku světýlka: kousek pájivého pole, tranzistor, fotorezistor, trimr nebo odpor, LED, odpor, držák 2× AA; orientačně 25–30 Kč na dítě.

## Postup lekce (osnova)

| Čas | Co dělají děti a vedoucí |
| --- | --- |
| 0–15 min | Připomenout LED a odpor z pasu součástek. Ukázka: kontaktní pole je „krabička s krokosvorkami uvnitř“ (vedoucí ukáže pípákem multimetru, které dírky jsou spojené). |
| 15–45 min | Dvojice: kartička ① trimr a ② fotorezistor. Multimetrem změřit fotorezistor na světle a ve tmě. Otázka: jak to obrátit, aby LED svítila ve tmě? |
| 45–60 min | **Tranzistor = kohoutek:** vedoucí ukáže na velkém nákresu. Dotykový spínač na jednom poli u vedoucího, každý si ho vyzkouší. |
| 60–100 min | Dvojice: kartička ③ světlo na tmu, ladění trimrem; nebo pájení výrobku, pokud se dělá. |
| 100–120 min | Pas součástek (fotorezistor, tranzistor), úklid součástek zpět do krabiček. |

## Bezpečnost

Jen bateriové napětí 3–4,5 V; proud přes prst u dotykového spínače je neškodný, ale nikdy nezkoušet na nic jiného než baterie. Drobné součástky nedávat do pusy. Při pájení výrobku jako obvykle.

## Po lekci

- **Vzorek:** typ tranzistoru, hodnota odporu do báze, jak spolehlivě funguje dotykový spínač na 3 V.
- **Skupina A:** zvládly dvojice kontaktní pole podle kartiček? Kolik zapojení muselo opravovat vedoucí?
- **Skupina B:** úpravy.
