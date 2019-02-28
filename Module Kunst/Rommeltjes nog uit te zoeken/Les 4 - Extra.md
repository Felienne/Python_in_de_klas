

### Maak een vierkant en zeshoek maar dan anders (extra)

Vorige week heb je een vierkant gemaakt, zo:

```python
for i in range(4):
  pen.forward(100)
  pen.left(90)
```

Typ die code weer even in, vanaf daar gaan we verder.

Waarom moet je bij een vierkant eigenlijk 90 graden draaien? Dat komt omdat een heel rondje rond 360 is.

Als je een vierkant wilt moet je dus 360 gedeeld door 4 = 90 graden draaien.

**Opdracht.** Verander je code eens om een zeshoek te maken.

Je moet nu twee regels veranderen. Kijk goed welke twee! Die moet je straks weer aanpassen.



**Opdracht.** Als je een zeshoek wilt, hoeveel graden moet je dan draaien?

```_________```


**Opdracht.** En welk sommetje moet je uitrekenen om aan dat antwoord te komen?

``` _________```



**Opdracht.** Schijf dat sommetje nu eens op in Python. Het komt straks tussen de ronde haakjes van ```pen.left()```

Denk eraan, in Python is een gedeeld door de slash /. Die zit bij de pijtjestoetsen op je toetsenbord.

```pen.left(......................)```



**Opdracht.** Voeg nu een variabele toe. De variabele heet 'aantal_hoeken'. Jij moet het zo programmeren dat je bij aantal_hoeken = 4 een vierkant krijgt, bij aantal_hoeken = 6 een zeshoek enzovoorts.

Je code zal er ongeveer zo uit zien:

```python
aantal_hoeken = 4

for i in range(...):
  pen.forward(100)
  pen.left(...)     #<-- hier komt het sommetje dat je hierboven hebt bedacht.
```

Deze les wordt afgetekend als:

- Je een vierkant hebt getekend
- De opdrachten pen.forward(100) en pen.left(90) ieder maar 1 keer gebruik zijn
- Er een for-opdracht in je code staat
- Er een variabele 'aantal_hoeken' is die op 4 ingesteld is en gebruikt wordt om de hoek te berekenen.

 <div style="page-break-after: always;"></div>

### Teken een figuur met invoer! (extra)

Met de code ```aantal_hoeken = int(input("hoeveel hoeken moeten er in het figuur komen?"))``` kun je de gebruiker van je programma vragen om iets in te voeren. Zet deze code bovenaan je programma en probeer het uit.

Let op! Je moet nu aan de rechterkant van je scherm wisselen naar 'console' om daar een getal in te typen. Daarna ga je terug naar de tekentool om het figuur te zien.

Maak nu een tweede variabele, die je grootte noemt.

 Zorg ervoor dat de variabele ook gebruikt wordt om het figuur te tekenen! Dus een groter getal moet een groter figuur opleveren. Pas ook de zin aan waarmee je de gebruikt vertelt wat hij of zij moet doen.

Deze opdracht wordt afgetekend als:

- Je een getal kan invoeren en je een figuur met precies dat aantal hoeken krijgt.
- Je een tweede getal kan invoeren dat de grootte bepaalt

 <div style="page-break-after: always;"></div>

### Meerdere figuren (extra)

Maak nog een derde invoervariabele.  Die gaat bepalen **hoeveel** figuren er in beeld komen.

Kijk goed naar de code die je al hebt!

Tip: er komt nu nog een forlus bij, om de lus die je al hebt.

Zorg ervoor dat er geen streepjes tussen de figuren komen door de pen omhoog en omlaag te doen op het juiste moment.

Je mag zelf kiezen waar de figuren komen, op willekeurige plekken, of in een nette rijn naast elkaar.

Deze opdracht wordt afgetekend als:

- Je een getal kan invoeren en je een figuur met precies dat aantal hoeken krijgt.
- Je een tweede getal kan invoeren dat de grootte bepaalt
- Je een derde getal kunt invoeren dat het aantal figuren instelt
- Er geen streepjes tussen de figuren zitten

 <div style="page-break-after: always;"></div>

### Schalen maar (extra)

Als je veel grote figuren instelt, zul je zien dat ze niet meer goed op het scherm passen. Daar gaan we nu wat aan doen. We willen het zo maken dat de grootte automatisch bepaald wordt! Dus als je 100 figuren bestelt met een invoer 100 dat krijg je kleine figuren, als je er maar 1 bestelt, dan krijg je een lekker grootte.

Haal de tweede invoer weg, er zijn dus nog maar 2 invoeren mogelijk:

1) Het aantal hoeken
2) Het aantal figuren

Zorg er nu voor dat de figuren groter worden als het er weinig zijn en kleiner als het er meer zijn.

**Tip:** je moet nu twee getallen door elkaar delen. Dat doe je in de code ```pen.forward(........)``` Delen doe je met de slash /.




Deze opdracht wordt afgetekend als:

- Je een getal kan invoeren en je een figuur met precies dat aantal hoeken krijgt.
- Je een **tweede** getal kan invoeren dat het aantal figuren instelt
- Je grotere figuren krijgt als je minder figuren print en kleinere als je er meer bestelt
- Er geen streepjes tussen de figuren zitten

 <div style="page-break-after: always;"></div>