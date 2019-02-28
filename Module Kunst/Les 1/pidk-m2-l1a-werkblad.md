### Figuren tekenen

Aan het einde van de les kun jij:

- systematisch een vierkant tekenen
- systematisch een driehoek tekenen
- systematisch een spirograaf tekenen
- de bijbehorende Python-code schrijven
- goede en foute print-codes vinden



**Teken verschillende figuren**

1) Maak een vierkant

Voor we aan het programmeren gaan, gaan we eerst op papier oefenen. Teken een vierkant in je schrift, maar… doe het precies volgens dit schema! 

**Let op:** Maak je vierkant lekker groot, minstens een halve pagina in je schrift. Want je moet er straks Python codes bij zetten.

- Begin in de tekenrichting 'rechts'
- Ga 5 cm in de tekenrichting (rechts nu dus)
- Draai 90 graden linksom
- Ga 5 cm volgens de tekenrichting (dat is nu omhoog)
- Draai 90 graden linksom
- Ga 5 cm volgens de tekenrichting (dat is nu links)
- Draai 90 graden linksom
- Volgens de tekenrichting (dat is nu omlaag)
- Draai 90 graden linksom

2) Maak een driehoek

Teken een driehoek, maar doe het weer volgens dit schema.

- Begin in de tekenrichting 'rechts'
- Ga 5 cm in de tekenrichting (rechts nu dus)
- Draai **120** graden linksom 
- Ga 5 cm volgens de tekenrichting (dat is nu schuin links-omhoog)
- Draai **120** graden linksom
- Ga 5 cm volgens de tekenrichting (dat is nu schuin rechts-omlaag)
- Draai **120** graden linksom





**Tekenen en code**

1) Teken een vierkant. Ga terug naar het vierkant dat je hebt getekend in je schrift. 
Zet deze nummers erbij, op dezelfde plek.

![image-20181207103857118](/Users/Felienne/Library/Application%20Support/typora-user-images/image-20181207103857118.png)

Om dit in Python te tekenen, heb je deze twee opdrachten nodig:

- pen.forward(100)
- pen.left(90)

Zet jij deze opdrachten bij de juiste plekken in de tekening? Je moet iedere opdracht vier keer gebruiken. Schrijf de codes op volgorde op in je schrift.

1. ...
2. ...
3. ...
4. ...
5. ...
6. ...
7. ...
8. ...



2) Maak een driehoek

Hier staat een driehoek.

![image-20181207104217890](/Users/Felienne/Library/Application Support/typora-user-images/image-20181207104217890.png)

1. Welke som reken je uit om een driehoek te maken? Schrijf de som in je schrift.

2. Welke Pythoncode gebruik jij voor de hoek van een driehoek? Vul het in op de puntjes.

pen.left(……..)

3. Een driehoek maak je met:

- pen.left(……..) <-- hier komt het getal dat je bij opdracht 1 hebt berekend
- pen.forward(100)

Zet jij nu deze opdrachten bij de juiste plekken in de tekening? Je moet allebei de Python opdrachten drie keer gebruiken. Schrijf het hier op:

1. ...
2. ...
3. ...
4. ...
5. ...
6. ...



3) Nog wat sommen met hoeken

Reken uit in je schrift: 

* Hoeveel moet je draaien voor een zeshoek?
* Hoeveel moet je draaien voor een tienhoek?
* Hoeveel moet je draaien voor een zesendertighoek?
* Hoeveel moet je draaien voor een dertighoek?


**Een niet-passende hoek**

1) Maak een spirograaf

Kies nu een eigen getal, waardoor 360 niet mooi deelbaar is. Schrijf je getal in je schrift.

Teken nu het figuur dat bij die hoek hoort.

- Begin in de tekenrichting 'rechts'
- Ga 5 cm in de tekenrichting (rechts nu dus)
- Draai **...** graden linksom <— hier komt jouw getal

Doe dit een paar keer, minstens 10!





-----



Voor in de slides:

Nu gaan we uitvinden wat er gebeurt als we een hoek kiezen waardoor 360 niet mooi deelbaar is. Laat leerlingen eens zo'n getal verzinnen (met wisbordjes bij voorkeur). 



Kies een leuk getal (bijv 100) en teken zelf het figuur op het bord.

In het begin zit het er een beetje gek uit:

![image-20181207082849999](/Users/Felienne/Library/Application%20Support/typora-user-images/image-20181207082849999.png)

Maar na naar een aantal stappen krijg je dit:

![image-20181207082814644](/Users/Felienne/Library/Application%20Support/typora-user-images/image-20181207082814644.png)



Dit is voor de slides:

**Vierkant**



Doe deze stappen zelf op het bord voor. Het is ideaal als je bij wiskunde even zo'n grote geo leent om het duidelijk voor te doen. Wat ik zelf ook doe:

- afstanden bij de lijnen
- in een andere kleur de draai aangeven, met de richting en het aantal graden

Dat ziet er dan zo uit:

![image-20181207090524855](/Users/Felienne/Library/Application%20Support/typora-user-images/image-20181207090524855.png)

**Driehoek**

Nu gaan lln op papier een **driehoek** maken. 

Leg uit/herhaal dat een figuur dat terug op zijn beginpunt komt, altijd hieken van samen 360 graden heeft. 





"Kijk maar een vierkant is 90 + 90 + 90 + 90, dan ben ik dus 'rond'. Als ik nu drie hoeken wil, welke som moet ik dan oplossen (dat is 360/3). Wat is 360/3? Nou 120"

Nu gaan we lln vragen een (gelijkzijdige) driehoek te tekenen op dezelfde manier als we het vierkant deden. 90 graden lukte misschien nog wel zonder geo, maar nu zullen ze echt moeten gaan meten, anders wordt het niks bij de meesten.



-----





**Klassikale uitleg Python Turtle**

Nu de leerlingen bekend zijn met de opdracht, en hun voorkennis van hoeken geactiveerd hebben, is het tijd om wat Python te gaat oefenen. Ook met Python kun je tekenen, dat gaat met iets dat 'Turtle' heet.

Ga naar deze Python-code: https://repl.it/@Felienne/Kunstles-start



Dit staat al voor je klaar:

```python
import turtle

pen = turtle.Turtle() # hier maken we de pen aan, dat is het driehoekje dat tekent
pen.speed(1) # zet de snelheid langzamer, dan zie je alles beter
```

Deze code is het al het ware verplicht om de tekentool op te starten. Spreek goed met leerlingen af dat ze hier niet aan rommelen want dan werkt het niet meer goed.

Onder deze regels kan het echte tekenen beginnen. Dezelfde dingen die we op papier hebben gedaan, kunnen ook in Python, met deze codes:

- ```pen.forward(10)``` betekent ga 10 vooruit. Niet 10 cm, maar 10 pixels! 100 is een betere voorbeeld voor op het digibord, anders zien lln het niet goed.
- ```pen.left(90)``` betekent draai de pen linksom, 90 graden

Met die stappen kunnen we dus al een vierkant tekenen. 

Doe dat eerst voor op het bord, waarbij je duidelijk aangeeft welke stappen welke betekenis hebben in Python, ik doe dat zo:

![image-20181207094109380](/Users/Felienne%201/Library/Application%20Support/typora-user-images/image-20181207094109380.png)



Als ze dit goed onder de knie hebben, dan kun je de Python code onderaan het document toevoegen:

```python
pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)
```



De lege regels hoeven niet, maar ik vind ze wel overzichtelijk, zo zie je goed dat het vier stappen zijn.



Dit gaan leerlingen ook oefenen op hun aftekenvellen, dus het is goed als ze dit even voor zich zien.

Nog een aantal tips:

- Lees de codes nog even hardop:
  - pen punt forward ronde haak openen 10 ronde haak sluiten
  - pen punt left ronde haak openen 90 ronde haak sluiten
- Stip ook even de betekenissen (en uitspraak) hier aan:
  - forward betekent "ga vooruit"
  - left betekent links, maar in deze code betekent het "draai linksom", dus niet "ga naar links"

Na deze uitleg kun je de leerlingvellen met lesdoelen 2, 3, 4 en 5 uitdelen!