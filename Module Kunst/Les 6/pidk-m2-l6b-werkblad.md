### Opdracht 6b-1) Maak je tekening!

Je hebt de afgelopen weken een hoop geleerd. Nu is het tijd om een mooie tekening te maken. 

**Je krijgt hiervoor een cijfer.**  

**Lever een link naar je programma in voor vrijdag 13:00 via Magister.**

Deze dingen moeten in je programma zitten voor een voldoende:

- Minstens 5 ***losse*** figuren.
- Minstens 3 variabele die je definieert én gebruikt.
- Minstens 3 kleuren.
- Netjes commentaar bovenaan.
- Bij moeilijke stukjes code ook commentaar achter de codes.



Je kunt extra punten verdienen door:

- Het gebruiken van rgb-codes voor kleuren.
- `begin_fill()` en `end_fill` om vlakken in te kleuren. 
- figuren met meerdere kleuren (zie onderaan dit werkblad)
- Andere coole dingen die je kunt verzinnen!

### Opdracht 6b-2) Wat vond je ervan?

We willen graag weten wat jij van de lessen tot nu toe vond.

Schrijf in je schrift de **drie dingen** die je het leuk vond.
Schrijf ook op wat je het minst leuk vond.



###Meerdere kleuren (extra)

Je kunt ook figuren tekenen met 1 kleur, en invullen met een andere kleur! 

![image-20190507095522235](../../img/image-20190507095522235.png)

Dat doe je door twee kleuren in te voeren in `pen.color()`. Zo dus:

```python
pen.color('orange', 'blue')
pen.begin_fill()

for i in range(50):
  pen.forward(100)
  pen.left(110)

pen.end_fill()
```

Je mag ook twee rgb-codes gebruiken in `pen.color()` maar let op! Dan moeten ze wel allebei tussen haakjes staan:

```python
pen.color((248,24,148), (64,224,208))
pen.begin_fill()

for i in range(60):
  pen.forward(100)
  pen.left(93)

pen.end_fill()
```
Dat maakt dit figuur:

![image-20190507100430580](../../img/image-20190507100430580.png)