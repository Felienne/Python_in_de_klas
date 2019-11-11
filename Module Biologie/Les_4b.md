### 1) Code tot nu toe

Deze opdracht wordt afgetekend als:

- Je voor alle blokken code in je schrift hebt geschreven wat ze doen

Hier lees je een paar stukken van de basiscode tot nu toe. 

**Let op!** Niet alle code staat in dit overzicht, lees dus goed. De codes staan ook niet in de goede volgorde.

Schrijf weer per blok in je schrift wat de code doet. Je mag hiervoor samenwerken met je buur. Je mag ook zeker kijken bij je uitwerkingen van vorige week.


```python
------- Blok 1 ------
while True:
```

```python
------- Blok 2 ------
muis = pygame.image.load("muis.png")
muis_rechthoek = muis.get_rect()
muis_snelheid = [1, 1]
```

```python
  ------- Blok 3 ------
  screen.blit(muis, muis_rechthoek)
  muis_rechthoek = muis_rechthoek.move(muis_snelheid)
```

```python
------- Blok 4 ------
kaas = pygame.image.load("kaas.png")
kaas_rechthoek = kaas.get_rect()
```

```python 
  ------- Blok 5 ------
  pygame.display.flip()
  screen.fill(backgroundColor)
```

```python
  ------- Blok 6 ------
  time.sleep(10 / 1000)
```

```python
  ------- Blok 7 ------
  if muis_rechthoek.bottom < 0:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.bottom > 600:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.right < 0:
      muis_snelheid[0] = - muis_snelheid[0]

  if muis_rechthoek.right > 800:
      muis_snelheid[0] = - muis_snelheid[0]
```
```python    
  ------- Blok 8 ------
  screen.blit(leeuw, leeuw_rechthoek)
  leeuw_rechthoek = leeuw_rechthoek.move(leeuw_snelheid)
```
```python
  ------- Blok 9 ------  
  screen.blit(kaas, kaas_rechthoek)
```
Nu komt de nieuwe code waar de muis groeit als hij kaas eet
```python
  ------- Blok 10 ------
  if muis_rechthoek.colliderect(kaas_rechthoek):
    print('hap hap')
```
```python
    ------- Blok 11 ------
    #de muis wordt groter:
    x, y = muis_rechthoek.size
    center = muis_rechthoek.center
```
```python
    ------- Blok 12 ------
    x, y = int(x * 1.05), int(y * 1.05)
    muis = pygame.image.load("muis.png")
```
```python
    ------- Blok 13 ------
    muis = pygame.transform.scale(muis, (x, y))
    muis_rechthoek = muis.get_rect()
    muis_rechthoek.center = center
```
###2) Weg met de muis

Deze opdracht wordt afgetekend als:

- Er "hap hap" in beeld komt via de *console* als het prooidier het voedsel raakt 
- Het prooidier na 3 seconden weer rechteronderhoek verschijnt

**Uitleg.** De muis blijft nu maar groeien en groeien, omdat hij steeds de kaas aanraakt. Dat is niet zo mooi. Zorg dat de muis (of jouw eigen dier natuurlijk) verplaatst naar de rechteronderhoek als hij een hapje kaas heeft genomen. 
Verander daarvoor de regel 
`muis_rechthoek.center = center` in
`muis_rechthoek.center = (...,...)` 

Op de stippeltjes moeten de goede getallen komen. Wat zou ongeveer de rechteronderhoek zijn? Probeer  getallen uit tot je tevreden bent.

###3) Eten maar!

Deze opdracht wordt afgetekend als:

- Er "hap hap" in beeld komt via de *console* als het prooidier en het roofdier elkaar raken
- Het prooidier verdwijnt als hij de roofdier aanraakt
- Het prooidier na 3 seconden weer linksboven verschijnt

**Uitleg.** Misschien heb je deze opdarcht vorige week al afgerond. Dan mag je meteen stempelen en door met de volgende opdracht.

###4) Het roofdier groeit ook

Deze opdracht wordt afgetekend als:

- Het prooidier ook groeit als hij voedsel eet

**Uitleg.** Kijk goed naar de code van het prooidier (de muis in het voorbeeld) en gebruik die code ook als het roofdier het prooidier aanraakt.

###5) Mooie randen (extra)

Deze opdracht wordt afgetekend als:

- De dieren niet meer uit beeld lopen boven en links

**Uitleg.** Het stuiteren van de eerste lessen werkt wel, maar niet zo mooi. Aan de onderkant en aan de rechterkant blijven de dieren in beeld als ze stuiteren. Maar boven en links niet. Kan jij dat oplossen?

Tip: Er zijn twee manieren om dit te doen. 
Manier 1: verander de getallen in de ifs.
Marnier 2: gebruik top ipv bottom, en gebruik left ipv right

Als je het extra spannend wilt maken, probeer je eens of je allebei de manieren werkend kunt krijgen.

### 6) Eigen stempeldoel (extra)

Deze opdracht wordt afgetekend als:

- Je zelf een doel hebt bedacht, en dat hebt uitgevoerd

**Uitleg.** Verzin zelf iets wat er nog bij kan in je simulatie. Een achtergrond? Een extra dier? Een kangaroe met een bokshandschoen? Bedenk iets en schrijf dat in je schrift. Voer het vervolgens netjes uit. Vraag wel eerst of mevr. Hermans je doel goed vindt.