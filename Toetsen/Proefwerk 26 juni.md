## Eindproefwerk Codasium



1) Wat is de fout?

Al deze codes zijn fout. **Schrijf op wat de fout is.**

```python
prnt('Hallo', 'allemaal')





```

```python
2. print('Hallo' , allemaal')
```

```python
3. for i in range(4)
     print('Hallo')
```

```python
4. namen = ['Neomai', 'Edgar', 'Rik', 'Sky']
   print(namen[4])
```

```python
5. begin_temperatuur = '12'
   extra = 10
   print(begin_temperatuur + extra)
```

2) Schrijf de Python code op om deze drie lijsten te maken:

* lijst `cijfers` met daarin de **getallen**: 8 6.5 10 
* lijst `vakken` met daarin de **woorden**: Gym, Technasium, Coderen
* lijst `engelse_woorden`. Verzin zelf 3 Engelse woorden om in je lijst op te slaan

3) Wat wordt er uitgeprint?

**Let op! Soms komt er een fout! Schrijf dan FOUT.**

```python
1.  dieren = ['konijn', 'biggetje', 'vleermuis']            
    print(dieren[3])
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
    print(namen[1], 'is', 'mijn', 'beste', 'vriend')
```

4) Wat printen deze codes met if-else erin? **Er kunnen ook weer fouten in zitten.** Schrijf dan FOUT.

De invoer van de gebruiker staat steeds naast de eerste regel

```python
1. if input('hond of kat') == 'hond':        INVOER: kat
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
3. if input('eend of kikker') == 'eend':     INVOER: Eend
     print('kwak')
   else:
     print('kwek')
```

```python
4. if input('eend of kikker') == 'eend'      INVOER: kikker
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

5) Wat tekenen deze codes? Teken de uitvoer van deze programma's.

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
for i in range(8):
pen.forward(100)
pen.left(45)
```


<div style="page-break-after: always; visibility: hidden">  </div>
6) Welke codes horen bij deze tekeningen? 

Het grootste figuur in de tekening is altijd getekend met `pen.forward(100)` Je mag de groottes van de andere figuren een beetje schatten, dat hoeft niet perfect te kloppen.



1.![image-20190624092159816](/Users/Felienne/Library/Application Support/typora-user-images/image-20190624092159816.png) <br>
2.![image-20190625142831568](/Users/Felienne/Library/Application Support/typora-user-images/image-20190625142831568.png)<br>
3.![image-20190624091900478](/Users/Felienne/Library/Application Support/typora-user-images/image-20190624091900478.png)<br>
4.![image-20190624092102182](/Users/Felienne/Library/Application Support/typora-user-images/image-20190624092102182.png)<br>

<div style="page-break-after: always; visibility: hidden">  </div>
7) Wat doen deze codes? Let op! **Leg het in woorden uit.** 

```python
hoek = 60
for i in range(6):
  pen.forward(50)
  pen.left(hoek)
```

Jouw antwoord: "Deze code tekent een zeshoek".
Nu jij:

```python
1.
aantal_keer = 6
for i in range(aantal_keer):
  pen.forward(50)
  pen.left(60)

pen.penup()
pen.forward(100)
pen.pendown()

aantal_keer = 3
for i in range(aantal_keer):
  pen.forward(50)
  pen.left(120)
```

```python
2.
aantal_keer = 8
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(45)
  
for i in range(aantal_keer):
  pen.forward(50)
  pen.left(45)
```

```python
3.
for i in range(aantal_hoeken):
  pen.forward(50)
  pen.left(hoek)
```

8) Welke kleur wordt dit? 

```python
1. pen.color(255, 0, 0)
2. pen.color(0, 255, 0)
3. pen.color(255, 255, 0)
4. pen.color(0, 0, 180)
5. pen.color(255, 0, 255)
```

9) Wat is het datatype van deze variabelen? **Kies steeds uit string, float of integer**.

```python
1. temperatuur = 21.9
2. naam = 'Hermans'
3. cijfer = 9
4. proefwerk = 'Codasium'
5. cijfer = 9.5
6. naam = 14
7. temperatuur = 18
```