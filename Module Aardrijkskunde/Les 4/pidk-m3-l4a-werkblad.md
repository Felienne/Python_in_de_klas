<img src="../../img/Logo cs-certificate.jpg" style="zoom:20%" align="right">

### Module Aardrijskunde Les 4 Werkblad a

### Aardbevingen plotten

Aan het einde van de les kun jij:

- Aardbevingen plotten op een wereldkaart met Python

**Even opfrissen!**

Vorige week hebben we geleerd hoe  datatypes kunnen omzetten zodat de tekst als een string ingelezen wordt en de cijfers als een float.

<u>Opdracht</u>

Vul de juiste functienaam in op de puntjes. Neem de stukjes code over in je schrift. De comments hoef je niet over te schrijven.

1) Hoe heet de functie waarmee we een ingelezen stuk tekst kunnen omzetten naar een heel getal? 

```python
magnitude = '5' #magnitude is nu een string van het karakter 5
magnitude_als_integer = ...(magnitude) #vul de juiste functienaam in op de puntjes
```

2) Hoe heet de functie waarmee we een ingelezen stuk tekst kunnen omzetten naar een kommagetal? 

```python
magnitude = '6.5' #magnitude is nu een string van de karakters 6.5
magnitude_als_float = .....(magnitude) #vul de juiste functienaam in op de puntjes

```

3) Probeer hetzelfde voor een longtitude waarde. 

```python
longtitude = '-173.972' #latitude is nu een string van de karakters -20.579
longtitude_als_float = .....(latitude) #vul de juiste functienaam in op de puntjes
```

 <div style="page-break-after: always;"></div>

4) Laten we nog even checken of we zelf wel herkennen met wat voor datatype we te maken hebben. Schrijf voor elk van onderstaande regels op om wat voor datatype het gaat

```python
1. 'latitude'

2. -18.569

3. 5.6

4. '6.3'

5. 3

6. '-20.579'
```

5)

Wat gebeurt er als we onderstaand stukje code willen uitvoeren?

```python
magnitude = '6'
magnitude_plus_5 = magnitude + 5 
print(magnitude_plus_5)
```

6) Wat gebeurt er als we onderstaand stukje code willen uitvoeren?

```python
magnitude = 5
magnitude_plus_5 = magnitude + 5 
print(magnitude_plus_5)
```

7) 

Wat gebeurt er als we onderstaand stukje code willen uitvoeren?

```python
magnitude = '6'
magnitude_plus_5 = float(magnitude) + 5 
print(magnitude_plus_5)
```

8) 

Wat gebeurt er als we onderstaand stukje code willen uitvoeren? *Let goed op bij deze!* 

```python
magnitude = '6.5'
magnitude_plus_5 = int(magnitude) + 5 
print(magnitude_plus_5)
```

 <div style="page-break-after: always;"></div>

Onderstaand plaatje is een stukje van de data over aardbevingen die de gaan inlezen te vinden is. 

<img src="../../img/data.png"
style="zoom:50%">

<u>Opdracht</u>

9) Maak de code hieronder af zodat de data van de vierde regel in opgehakte stukjes in een lijst komt te staan. Dat is de aardbeving die op 1/8/65 plaatsvond. Dit hebben wevorige week ook geoefend.

```python
data = inlezen(target_url)

regel_4 = data[...]

lijst_van_opgehakte_regel_4 = regel_1.split(... ... ...) #vul de missende tekens in op de stippellijnen.
```

 <div style="page-break-after: always;"></div>

10) Lees nu voor elk van de kolommen de data van deze regel in. Gebruik hiervoor de het resultaat wat in het stukje hierboven in regel_4 staat. Overal waar puntjes staan mist nog code die jij moet invullen. Neem alles over in je schrift.

```python
1. magnitude = ....(lijst_van_opgehakte_regel_4[...])

2. longtitude = ....(.........................[3])

3. latitude = ....(lijst_van_opgehakte_regel_4[...])

4. depth = ....(lijst_van_opgehakte_regel_4[...])

5. time = lijst_van_opgehakte_regel_4[...]

6. date = lijst_van_opgehakte_regel_4[...] 
```

------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel 

------

 <div style="page-break-after: always;"></div>

**Turtle en for-loop geheugen opfrissen!**

1) Wat doen deze codes? Leg het in je eigen woorden uit. 

```python
1.
hoek = 60
for i in range(6):
  pen.forward(50)
  pen.left(hoek)
  
hoek = 90
for i in range(4):
  pen.forward(50)
  pen.left(hoek)
```

```python
2.
aantal_keer = 6
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(60)
```

```python
3.
aantal_keer = 6
hoek = 60
for i in range(aantal_keer):
  pen.forward(50)
  pen.left(hoek)
```

Laten we ook even ons geheugen opfrissen over de kleuren.

4) Wat tekenen deze codes? Gebruik kleurpotloden of stiften. Heb je die niet? Zet dan de namen van de kleuren in de tekening.

```python
1. pen.color(255, 0, 0)
2. pen.color(0, 255, 0)
3. pen.color(160, 0, 0)
4. pen.color(160, 0, 0)
5. pen.color(160, 160, 0)
6. pen.color(0, 160, 0)
```

------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel 

------

 <div style="page-break-after: always;"></div>

**Aardbevingen plotten**

Voor we straks aan de slag gaan op de computer, gaan we nog éven wat oefeningen doen. 

1) Vertaal onderstaande zinnen code naar 'mensen' taal. Ofwel: leg uit wat er gebeurt.

```python
1. for line in data:
```

```python
2. pen.goto(longtitude, latitude)
```

```python
3. pen.dot(magnitude)
```

2) Dit plaatje is weer een stukje van de data over aardbevingen die we gaan inlezen te vinden is. 

<img src="../../img/data.png"
style="zoom:50%">

Vul de missende stukjes code in op de stippellijnen

```python
pen = turtle.Turtle()
pen.color("green")

data = inlezen(target_url) #vul de missende code in op het stippellijntje

for line in ....: #vul de missende code in op het stippellijntje
  earthquake = line.split(',')
  longtitude = earthquake[...] #vul de missende code in op het stippellijntje
  latitude = earthquake[2]
  magnitude = float(earthquake[6])
    
  pen.penup()
  pen.goto(longtitude, ........)  #vul de missende code in op het stippellijntje
  pen.pendown()
  pen.dot(........)  #vul de missende code in op het stippellijntje
```

