<img src="/Users/lisa/Python_in_de_klas/Module-Aardrijkskunde/Les 1/Logo cs-certificate.jpg"
style="zoom:20%" align="right">

### Module Aardrijskunde Les 2 Werkblad a

### Data inlezen in Python

Aan het einde van de les kun jij:

- Tekst inlezen uit een bestand
- Tekst netjes laten ophakken in stukjes

In deze lessen ga jij zelf data over aardbevingen door Python laten inlezen. De data die we binnen krijgen gaan we leren ophakken in stukjes zodat we de data kunnen gebruiken om onze aardbevingen te plotten. Op dit werkblad maken we eerst opdrachten met pen en papier.

**Even opfrissen!**
Vorige week hebben we geleerd hoe we de data van een aardbeving kunnen lezen. 

<img src="/Users/lisa/Python_in_de_klas/Module-Aardrijkskunde/Les 1/data.png"
style="zoom:70%">

1) Schrijf per kolom op wat dit vertelt over de aardbeving

1. Date = ......

2. Time = ......

3. Latitude = ......

4. Longtitude = ......

5. Type = ......

6. Depth = ......

7. Magnitude = ......

2) Vul de missende getallen in.

1. De latitude gaat van -... graden tot +... graden

2. De longtitude gaat van -... graden tot +... graden

------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel 

------

**Data inlezen**

We gaan nu oefenen met het inlezen van data. Onderstaand is wederom een stukje van de data die in de target_url te vinden is. 

<img src="/Users/lisa/Python_in_de_klas/Module-Aardrijkskunde/Les 1/data.png"
style="zoom:70%">

```python
target_url = 'aardbevingen_data.csv' # Dit is 'zogenaamd' de code die aangeeft waar dit bestand terug te vinden is.
```

1) Welke van deze codes leest op de juiste manier de data uit de target_url in? 
Schrijf de goede code over in je schrift!

```python
- data = target_url

- data = readlines
        
- data = readlines(target_url)
        
- target_url = readlines(data)
```

Als je opdracht 1 goed hebt gemaakt, heb je python nu een hele lange lijst met data laten inlezen, dat ziet er ongeveer uit zoals hieronder. 
![image-20190520175053015](/Users/lisa/Python_in_de_klas/Module-Aardrijkskunde/Les 2/data_ingelezen.png)
2) Hoe zorgen we nu dat we alleen de eerste regel inlezen? Maak de code af en schrijf het over in je schrift.

```python
regel_1 = data... ... ... #vul de missende tekens en het missende cijfer in op de stippellijnen
```

3) Hoe zorgen we nu dat we alleen de derde regel inlezen? Schrijf de juiste code in je schrift.

4) we willen de aardbeving inlezen die plaatsvond op 12 januari 1965. Schrijf de juiste code in je schrift waarmee je deze aardbeving kunt inlezen. 

------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel 

------

**Data in stukjes hakken**

We hebben nu de data van de eerste aardbeving ingelezen 
![image-20190520175640059](/Users/lisa/Python_in_de_klas/Module-Aardrijkskunde/Les 2/data_regel_0_ingelezen.png)

1) Maak de code hieronder af zodat de data in opgehakte stukjes in een lijst komt te staan.

```python
lijst_van_opgehakte_regel_1 = regel_1.split(... ... ...) #vul de missende tekens in op de stippellijnen.
```

2) Hieronder staan vijf codes waarin een stukje data over de eerste aardbeving uit de afbeelding wordt geprint. Wat printen deze codes uit? Let op, er staan ook foute codes tussen! 

Schrijf de uitvoer in je schrift.

```python
1. print(lijst_van_opgehakte_regel_1[0])               
```

```python
2. print(regel_1[6])   
```

```python
3. magnitude = lijst_van_opgehakte_regel_1[6]
print(magnitude)
```

```python
4. print(lijst_van_opgehakte_regel_1[3])
```

```python
5. print(lijst_van_opgehakte_regel_1[7])
```

------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel 

------
