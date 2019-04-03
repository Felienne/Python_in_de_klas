### for en in

Aan het einde van dit werkblad kun jij:

- voorspellen wat Python code met een for erin doet
- goede en foute for lussen van elkaar onderscheiden

Spelregels:

- Denk niet te diep na over de codes, het gaat er om dat je het snel gaat kunnen
- Schrijf de codes over als daarom gevraagd wordt, juist door opschrijven oefen je goed
- Spieken/overschrijven is zinloos, het gaat juist om het oefenen. Snap je iets niet, vraag het dan aan ons

###for uitleg

Met een 'for-lus' kun je een actie uitvoeren voor ieder element in een lijst. Denk bijvoorbeeld aan de lijst `telwoorden` met daarin `['een', 'twee', 'drie']`.

We kunnen nu ieder woord uit de zin printen:

Een for ziet er zo uit:

```python
for woord in telwoorden:
  print(woord)
```
Deze code print":
```python
een
twee
drie
```

Je kunt ook meerdere dingen herhalen door ze allemaal in de lus te zetten:


```python
for woord in telwoorden:
  print('Hallo')
  print(woord)
```
Deze code print":
```python
Hallo
een
Hallo
twee
Hallo
drie
```

Soms wil je getallen uit een lijst niet alleen printen, maar er iets anders mee doen, zoals optellen. Daarvoor gebruik je een *accumulator*. Dat is een variabele waarin je  het resultaat bijhoudt. In dit voorbeeld is `som` de *accumulator*. 

```python
som = 0
metingen = [2,4,14,25,26,42]
for huidige_meting in metingen:
    som = som + huidige_meting
print(som)
```



Let op deze dingen:

- achter de regel met `for` hoort een dubbele punt :
- de variabele achter `for` neemt bij iedere herhaling de volgende waarde in de lijst aan, dus eerst de eerste en dan de tweede etc.
- regels onder de for beginnen met 2 spaties
  - alle regels die met 2 spaties beginnen horen bij de lus
  - die worden allemaal herhaald!

### Opdrachten

1) Je krijgt een aantal codes. Wat wordt er geprint? 

Voorbeeld:

```python
snacks = ['chips', 'taco', 'drop']
for s in snacks:
  print('Ik hou van', s)
```

Voor iedere snack `snack` in de lijst print de code 'Ik hou van' en dan de waarde van `snack`. Dus de code print: 

```python
Ik hou van chips
Ik hou van taco
Ik hou van drop
```

Nu jij! Let op, de codes kunnen ook fout zijn. Schrijf dan 'fout'.

```python
snacks = ['chips', 'taco', 'drop']
for s in snacks:
  print('Ik hou van', s)
  print('Echt lekker')
```

```python
fruit = ['appel', 'druif', 'banaan']
for f in fruit:
  print('Ik hou van', f)
print('Ook nog gezond')
```
```python
even_getallen = [2,4,6,8,10,12]
for getal in even_getallen:
  print(getal * getal)   #een sterretje is keer in Python
```
```python
even_getallen = [2,4,6,8,10,12]
for getal in even_getallen:
print(getal + 5)
```
```python
oneven_getallen = [1,3,5,7,9,11,13,15]
for getal in oneven_getallen
  print(getal + 10)
```
```python
even_getallen = [2,4,6,8,10,12]
for getal in even_getallen:
  print(getal - 4)
```

2) Nu een paar stukjes code met een accumulator erin. Wat printen deze codes?
```python
even_getallen = [2,4,6,8,10,12]
total = 0
for getal in even_getallen:
  total = total + getal * getal   #een sterretje is keer in Python
  print(total)
```
```python
even_getallen = [2,4,6,8,10,12]
average = 0
for getal in even_getallen:
  average = average + getal
print(average/6)  #/ is delen in Python
```
```python
even_getallen = [2,4,6,8,10,12]
totaal_verschoven = 4
for getal in even_getallen:
  totaal_verschoven = totaal_verschoven + (getal - 4)
print(totaal_verschoven)
```


### in

Je kunt in op twee manieren gebruiken, samen met een `for` om iets met ieder element in een lijst te doen, maar ook met een `if` om te kijken of een element in een lijst zit. Dat gaat zo:

```python
bingo_getallen = [2,4,14,25,26,42]
mijn_lot = 17
if mijn_lot in bingo_getallen:
  print('Ik heb gewonnen!')
else:
  print('Helaas toch gewoon naar school maandag.')
```

Deze code print nu 'Helaas toch gewoon naar school maandag.' Maar als 17 wel in de lijst `bingo_getallen` zit, dan zou de code 'Ik heb gewonnen!' printen.

2) Wat printen deze codes?

```python
kleuren = ['blauw', 'geel', 'groen', 'zwart']
if 'magenta' in kleuren:
  print('Ik ben roze, knalroze')
else:
  print('Liever een andere kleur hoor.')
```
```python
talen_bij_Liacs = ['Python', 'C++', 'HTML', 'shellscript']
mijn_lievelingstaal = 'QBasic'
if mijn_lievelingstaal in talen_bij_Liacs:
  print('Ik schrijf me meteen in!')
else:
  print('Maar ik hou zo van', mijn_lievelingstaal)
```
```python
getal = 19
even_getallen = [2,4,6,8,10,12]
if getal in even_getallen:
  print(getal/2)   #/ is gedeeld door in Python
else:
  print(getal-2)
```

```python
assortiment_bakker = ['appelflap', 'bananenbrood', 'halfje wit']
if 'worteltjestaart' in assortiment_bakker:
  print('Lekker he?')
else:
  print('Ow dan kom ik morgen wel terug')
```