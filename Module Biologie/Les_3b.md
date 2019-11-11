

### 1) Code tot nu toe

Deze opdracht wordt afgetekend als:

- Je voor alle blokken code in je schrift hebt geschreven wat ze doen

Hier lees je de basiscode tot nu toe. De code is opgedeeld in blokken, tussen de strepen. Schrijf per stuk in je schrift wat de code doet. Je mag hiervoor samenwerken met je buur.


```python
------- Blok 1 ------
import pygame
import time

------- Blok 2 ------
pygame.init()
breedte = 800
hoogte = 600
screen = pygame.display.set_mode((breedte, hoogte))
backgroundColor = 0, 0, 0

------- Blok 3 ------
muis = pygame.image.load("muis.png")
muis_rechthoek = muis.get_rect()
muis_snelheid = [1, 1]

------- Blok 4 ------
leeuw = pygame.image.load("leeuw-a.png")
leeuw_rechthoek = leeuw.get_rect()
leeuw_snelheid = [1, 1]

------- Blok 5 ------
while True:
  
  ------- Blok 6 ------
  pygame.display.flip()
  screen.fill(backgroundColor)

  ------- Blok 7 ------
  screen.blit(muis, muis_rechthoek)
  muis_rechthoek = muis_rechthoek.move(muis_snelheid)
  
  ------- Blok 8 ------
  if muis_rechthoek.bottom < 0:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.bottom > 600:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.right < 0:
      muis_snelheid[0] = - muis_snelheid[0]

  if muis_rechthoek.right > 800:
      muis_snelheid[0] = - muis_snelheid[0]
      
  ------- Blok 9 ------
  screen.blit(leeuw, leeuw_rechthoek)
  leeuw_rechthoek = leeuw_rechthoek.move(leeuw_snelheid)

  ------- Blok 10 ------
  if leeuw_rechthoek.bottom < 0:
      leeuw_snelheid[1] = - leeuw_snelheid[1]

  if leeuw_rechthoek.bottom > 600:
      leeuw_snelheid[1] = - leeuw_snelheid[1]

  if leeuw_rechthoek.right < 0:
      leeuw_snelheid[0] = - leeuw_snelheid[0]

  if leeuw_rechthoek.right > 800:
      leeuw_snelheid[0] = - leeuw_snelheid[0]

  ------- Blok 11 ------
  time.sleep(10 / 1000)
```



###2) Laad het programma in

Deze opdracht wordt afgetekend als:

- Je 2 dieren hebt die netjes door het veld bewegen en de randen niet raken.

Let op! Je kunt deze opdracht op 2 manieren doen. 

Optie 1: Je gaat naar je code van vorige week, als je al alles al af had.

Optie 2: Je begint vanaf de werkende code van mevr. Hermans en werkt vanaf daar verder. Die code staat hier: https://repl.it/@mevrHermans/simulatie-einde-week-2

Dan moet je wel je dierenplaatjes opnieuw uploaden.

### 3) Voeg voedsel toe

Deze opdracht wordt afgetekend als:

- Je een soort voedsel voor je prooidier hebt geupload
- Dat voedsel stil in het veld staat

Ook je prooidier (het dier dat gegeten wordt) moet eten. Voeg dus nu een plaatje van dat voedsel in, bijv. gras of kaas. Gebruik deze checklijst om te kijken of je alle code hebt gebruikt. Kijk steeds in de code die je al hebt (of de code hier boven) om te kijken hoe het precies moet.

1. Laad het plaatje in met `image.load` 
2. Maak een variabele van het plaatje met `get_rect`
3. Maak het plaatje zichtbaar met `blit`. 
   **Let op!** Blit moet in `while True:`dus met twee spaties ervoor!

###Samenvatting-----

Je hebt nu drie dingen in beeld staan:

* **Voedsel** voor je prooidier (in het voorbeeld is dat een kaas)
* Een **prooidier** (in het voorbeeld de muis)
* Een **roofdier** (in het voorbeeld de leeuw )

### 4) Eten 

Deze opdracht wordt afgetekend als:

- Er "hap hap" geprint wordt als je prooidier het eten aanraakt.

**Uitleg**

Gebruik de *'collision detection'* code om te kijken of het dier zijn voedsel aanraakt. De code werkt zo:

```python
muis_rechthoek.colliderect(kaas_rechthoek)
```

Maar dan natuurlijk met jouw dieren en jouw variabelen!

### 5) Eten-2 (Extra, sla over als je nog niet zo ver bent)

Deze opdracht wordt afgetekend als:

- Er "hap hap" in beeld komt via de *console* als het prooidier en het roofdier elkaar raken
- Het prooidier verdwijnt als hij de roofdier aanraakt
- Het prooidier na 3 seconden weer linksboven verschijnt

**Uitleg**

Nu ga je je if aanpassen zodat er niet alleen geprint wordt, maar ook iets anders gebeurt. Je kunt een dier verplaatsen met een move() commando, zo:

```python
muis_rechthoek = muis_rechthoek.move(..... , .....)
```

Wat moet er op de stippeltjes om jouw dier linksboven te laten verschijnen? 
Let op: Jouw dier is waarschijnlijk geen muis, dus pas ook de naam van de variabele aan!

###6) Groeien

Deze opdracht wordt afgetekend als:

- Er "hap hap" in beeld komt via de *console* als het prooidier en het roofdier elkaar raken
- Het prooidier groeit als hij voedsel eet
- Het prooidier omdraait als hij het voedstel aanraakt

**Uitleg**

Kijk goed waar er hap hap geprint wordt. Daar moet code bij om de muis te laten groeien. Dit is de code die je nodig hebt. Typ deze code precies over en let op! De code moet steeds met 4 spaties beginnen.

```python
    #de muis wordt groter:
    x, y = muis_rechthoek.size
    center = muis_rechthoek.center
    x, y = int(x * 1.05), int(y * 1.05)
    muis = pygame.image.load("muis.png")
    muis = pygame.transform.scale(muis, (x, y))
    muis_rechthoek = muis.get_rect()
    muis_rechthoek.center = center
    #de muis draait om:
    muis_snelheid[1] = - muis_snelheid[1]
    muis_snelheid[0] = - muis_snelheid[0]
```

###7) Groeien-2 (extra)

Doe vóór deze opdracht eerst Eten 2. 
Deze opdracht wordt afgetekend als:

- Ook het roofdier groeit als hij het prooidier aanraakt.

**Uitleg**

Bekijk de code hier boven goed en pas aan wat nodig is.

###8) Groeien-3 (extra)

Doe voor deze opdracht eerst Eten 2 en Groeien.
Deze opdracht wordt afgetekend als:

- Je voor alle regels code van "Groeien" in je schrift hebt geschreven wat ze doen

**Uitleg**

Bekijk de code hier boven goed en schrijf nu per regel op wat de code doet. Je mag hiervoor best Google gebruiken en overleggen met je buur. Schrijf het zo in je schrift:

1.    Hier wat regel 1 doet
2.    En dan hier wat regel 2 doet

enz.



