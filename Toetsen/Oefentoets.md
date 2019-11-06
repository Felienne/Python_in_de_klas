## Oefentoets



1) Wat is de fout?

Al deze codes zijn fout. Wat is er mis? 

Schrijf in je schrift **wat de fout is**. 

```python
1. prnt('Hallo', 'allemaal')
```

```python
2. print('Hallo' , allemaal')
```

```python
3. print('Hallo' 'allemaal')
```

```python
4. print 'Hallo Allemaal'
```

```python
5. prit('Hallo')
   prit('Allemaal')
```

2) Schrijf de Python code op om deze drie lijsten te maken:

* lijst `cijfers` met daarin de getallen: 8, 9, 7 en 10.
* lijst `vakken` met daarin de woorden: Frans, Aardrijkskunde, Coderen
* lijst `engelse_woorden`. Verzin zelf 3 Engelse woorden om in je lijst op te slaan

3) Wat wordt er uitgeprint?

**Let op! Soms komt er een fout! Schrijf dan FOUT.**

```python
1.  dieren = ['konijn', 'biggetje', 'vleermuis']            
    print(dieren[2])
```

```python
2.  dieren = ['konijn', 'biggetje', 'vleermuis']            
    print(dieren[0])
```

```python
3.  kleuren = ['blauw', 'geel', 'groen']            
    print('De', 'deur', 'is', kleuren[0])
```

```python
4.  hobbies = ['dansen', 'voetballen', 'zingen']            
    print('Ik', 'zit', 'op', hobbies[2])
```
```python
5.  namen = ['Jan', 'Robin', 'Samir']
    print namen[3], 'is', 'mijn', 'beste', 'vriend')
```

4) Wat printen deze codes met if-else erin? Er kunnen ook weer fouten in zitten.

De invoer van de gebruiker  staat steeds naadt de eerste regel

```python
1. if input('hond of kat') == 'hond':         INVOER: hond
     print('waf')
   else:
     print('miauw')
```

```python
2. if input('hond of kat') == 'kat':         INVOER: kikker
     print('miauw')
   else:
     print('waf')
```

```python
3. if input('eend of kikker') == 'eend':     INVOER: eend
     print('kwak')
   else:
     print('kwek')
```

```python
4. if input('eend of kikker') == 'eend':     INVOER: EEND
     print('kwak')
   else:
     print('kwek')
```

```python
5. if input('varken of koe') == 'koe':       INVOER: koe
     print('boe')
   else:
     print('oink')
```

5) Wat tekenen deze codes? 

**Let op! De codes kunnen ook fout zijn! Schrijf dan FOUT.**

```python
1.
for i in range(6)
  pen.forward(100)
  pen.left(60)
```

```python
2.
aantal_keer = 6
grootte = 100
for i in range(4):
  pen.forward(100)
pen.left(60)
```
```python
3.
aantal_hoeken = 8
hoek = 360/aantal_hoeken
for i in range(aantal_hoeken):
  pen.forward(50)
  pen.left(hoek)
```

```python
4.
for i in range(4):
  pen.forward(100)
  pen.left(90)
```

```python
5.
for i in range(4):
  pen.forward(100)
  pen.left(90)
```

6) Welke codes horen bij deze tekeningen? 


1. ![image-20190619075843187](/Users/Felienne/Library/Application Support/typora-user-images/image-20190619075843187.png)
2. ![image-20190619075853242](/Users/Felienne/Library/Application Support/typora-user-images/image-20190619075853242.png)
3. ![image-20190619075903775](/Users/Felienne/Library/Application Support/typora-user-images/image-20190619075903775.png)

7) Wat doen deze codes? Leg het in woorden uit. 

**Let op: Er kunnen nu ook foutjes in de codes zitten! Schrijf dan FOUT!**	

Voorbeeld!

```python
hoek = 60
for i in range(6):
  pen.forward(50)
  pen.left(hoek)
  
hoek = 90
for i in range(4):
  pen.forward(50)
  pen.left(hoek)
```

Jouw antwoord: "Deze code tekent een zeshoek, en daarna op dezelfde plek een vierkant."

```python
1.
aantal_keer = 6
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(60)
```

```python
2.
aantal_keer = 6
hoek = 60
for i in range(aantal_keer):
  pen.forward(50)
  pen.left(hoek)
```

```python
3.
aantal_hoeken = 3
hoek = 360/aantal_hoeken
for i in range(aantal_hoeken):
  pen.forward(50)
  pen.left(hoek)
```

**Kleuren tekenen**

8) Welke kleur wordt dit? Tip: lagere getallen zijn donkerder, niet lichter!

```python
1. pen.color(255, 0, 0)
2. pen.color(0, 255, 0)
3. pen.color(255, 255, 0)
4. pen.color(180, 0, 0)
5. pen.color(255, 0, 255)
```