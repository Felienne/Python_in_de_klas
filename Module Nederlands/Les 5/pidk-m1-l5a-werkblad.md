<img src="../../img/Logo cs-certificate.jpg" style="zoom:20%" align="right" />

## Les 5 werkblad a

Todos:

* nummerfoutjes
* uitvoer is geen goed woord
* waarom geen woorden apart in inpit()
* regels doorstrepen is beter, takken waren niet goed ingeoefend
### Les 5 werkblad a



### if-else

Aan het einde van de les kun jij:

-  invoer gebruiken in je programma met `input()`
-  je verhaal een ander verloop geven op basis van invoer met een if-else commando

**Even opfrissen!**

**Begin op een nieuwe pagina en zet erboven: Les 5a**

**Goed of fout?**

1) Is de code goed of fout?

* De code is goed -> schrijf wat de code print
* De code is fout -> schrijf FOUT
* Extra: schrijf ook **wat** er fout is

```python
1. hobbies = ['dansen', 'voetballen', 'zingen']            
   print('Zullen', 'we', 'gaan', hobbies[1], 'morgen')
```
```python
2. namen = ['Jan', 'Robin', 'Samir']
   print('Mijn', 'beste', 'vriend', 'heet', namen[0])
```
```python
3. talen = ['Python', 'JavaScript', 'HTML']
   print('De', 'beste', 'programmeertaal', 'is', taal[1])
```
```python
4. snoepjes = ['chocolade', 'zuurtjes', 'drop']
   print('Ik', 'hou', 'van', snoepjes(2))
```
```python
5. straatnamen = ['Witte Hertstraat', 'Takstraat', 'Coolsingel']
   print('Ik', 'woon', 'in', 'de', 'straatnamen[2]')
```

```python
6. hobbies = ['dansen', 'voetballen', 'zingen']            
   print('Ik', 'zit', 'op', hobbies[0])
```

```python
7. kleuren = ['blauw', 'geel', 'groen', 'paars', 'roze']            
   print('Mijn', 'trui', 'is', kleuren[5])
```
```python
8. namen = ['Jan', 'Robin', 'Samir']
   print(namen[3], 'is', 'mijn', 'beste', 'vriend')
```

```python
9. vakken = ['Aardrijkskunde', 'Nederlands', 'Coderen']
   print('Ik', 'vind', vakken[4], 'leuk')
```

```python
10.kleuren = ['blauw', 'geel', 'groen']            
   print('De', 'deur', 'is', kleuren[1])
```

```python
11.doelgroep = 'leerlingen'
   print('Hallo', doelgroep)
```

```python
12.naam = 'Jansen'
   #print('Hallo', 'meneer', naam)
```
```python
13. #klas = c              
   print('Leerlingen', 'uit', klas)
```
```python
14.dag = 'woensdag'
   print('Het', 'is', 'vandaag', 'woensdag')
```
 <div style="page-break-after: always;"></div>

2) Maak de code af

Je krijgt een zin, en jij moet de code afmaken. Je hoeft alleen de lijst en de aanwijzer in je schrift te schrijven. Voorbeeld:

Er moet geprint worden: 'Ik vind geel mooi' Maak de code af in je schrift. 

```python
   kleuren = ['blauw', 'geel', 'groen']            
   print('Ik', 'vind', kleuren[...], 'mooi')
```
Dan schijf jij in je schrift: kleuren[1]
Nu jij!

1. Er moet geprint worden: 'De trui is groen' Maak de code af in je schrift. 

```python
   kleuren = ['blauw', 'geel', 'groen']            
   print('De', 'trui', 'is', kleuren[...])
```

2. Er moet geprint worden: 'Ik hou van drop' 

```python
   snoepjes = ['chocolade', 'zuurtjes', 'drop']
   print('Ik', 'hou', 'van', snoepjes[...])
```

3. Er moet geprint worden: 'Zullen we gaan gamen morgen?'

```python
   hobbies = ['gamen', 'voetballen', 'zingen']            
   print('Zullen', 'we', 'gaan', hobbies[...], 'morgen?')
```

4. Er moet geprint worden: 'Mijn beste vriend heet Samir'

```python
   namen = ['Jan', 'Robin', 'Samir']
   print('Mijn', 'beste', 'vriend', 'heet', namen[...])
```

5. Er moet geprint worden: 'De beste programmeertaal is Python'

```python
   talen = ['Python', 'JavaScript', 'HTML']
   print('De', 'beste', 'programmeertaal', 'is', talen[...] )
```

6. Er moet geprint worden: 'Ik woon in de Takstraat'

```python
   straatnamen = ['Witte Hertstraat', 'Takstraat', 'Coolsingel']
   print('Ik', 'woon', 'in', 'de', straatnamen[...])
```

------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

Als je klaar bent mag je aan het Extra Opgaves blad gaan werken.

 <div style="page-break-after: always;"></div>

**if-else commandos**

1) Je krijgt een aantal codes, én de invoer van een gebruiker. 

Wat wordt er geprint? 

Voorbeeld:

```python
   if input('melk of suiker') == 'melk':  
     print('gieten')
   else:
     print('schudden')
   >melk of suiker?melk
```

De invoer is: melk (kijk bij de >)
De code print: gieten.
Nu jij!

```python
1. if input('melk of suiker') == 'melk': 
     print('gieten')
   else:
     print('schudden')
   >melk of suiker?suiker
```

De invoer is: suiker.
De code print: …….

```python
2. if input('melk of suiker') == 'melk': 
     print('gieten')
   else:
     print('schudden')
  >melk of suiker?pindakaas
```

De code print: …....

```python
3. if input('reptiel of zoogdier') == 'reptiel':
     print('legt', 'een', 'ei')
   else:
     print('geeft', 'melk')
   >reptiel, of, zoogdier?reptiel
```

De code print: …....

```python
4. if input('reptiel of zoogdier') == 'reptiel':
     print('legt', 'een', 'ei')
   else:
     print('geeft', 'melk')
   >reptiel of zoogdier?zepdiel
```

De code print: …....

```python
5. if input('reptiel of zoogdier') == 'reptiel':
     print('legt', 'een', 'ei')
   else:
     print('geeft', 'melk')
   >reptiel of zoogdier?zoogdier
```

De code print: …....

```python
6. if input('Nederlands of Engels') == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   >Nederlands of Engels?engelse
```

De code print: …....

```python
7. if input('Nederlands of Engels') == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   >Nederlands of Engels?Engels
```

De code print: …....

```python
8. if input('Nederlands of Engels') == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   >Nederlands of Engels?English
```

De code print: …....

```python
9. if input('Nederlands of Engels') == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   >Nederlands of Engels?Nederlands
```

De code print: …....

 <div style="page-break-after: always;"></div>


```python
10. if input('Nederlands of Engels') == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   >Nederlands of Engels?Nl
```

De code print: …....

2) Er zijn vijf dingen heel belangrijk bij een if-else. Schrijf er zoveel mogelijk op in je schrift.

3) Nu maak jij de if-else zelf.

We gaan steeds de goede dierengeluiden printen. Deze horen bij elkaar:

* hond - waf
* kat - miauw
* kikker - kwak
* eend - kwek
* koe - boe
* varken - oink

1) Wat moet er op de puntjes? Alleen dat hoef je in je schrift te schrijven. 

```python
1. if input('hond of kat') == 'hond':
     print(...)
   else:
     print('miauw')
```

```python
2. if input('hond of kat') ... 'kat':
     print('miauw')
   else:
     print('waf')
```

```python
3. if input('eend of kikker') == ...:
     print('kwak')
   else:
     print('kwek')
```


```python
4. if input('hond of kat') == 'hond':
     print('waf')
   else:
     print(...)
```

```python
5. if input('varken of koe') == 'koe':
     print('boe')
   else:
     print(...)
```



------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

Als je klaar bent mag je aan het Extra Opgaves blad gaan werken.

 <div style="page-break-after: always;"></div>

**Fouten bij if-else commando's**

1) Fout of niet? Lees de code plus invoer. Voorspel of er een fout komt, of niet. 

Komt er een fout, schrijf dan in je schrift: FOUT. 
Komt er geen fout, schrijf dan op wat de code print.

Voorbeeld:

```python
if input('Frans of Engels') == 'Frans':
  print('Bonjour!')
else:
   print('Hello!')
   >Frans of Engels?Frans
```

De code…. print 'Bonjour'
Voorbeeld:

```python
if input('Frans of Engels') == 'Frans'
  print('Bonjour!')
else:
   print('Hello!')
   >Frans of Engels?Frans
```

De invoer is: Frans.
De code…. is FOUT, want de eerste regel mist een :

Nu jij!

```python
1. if input('Frans of Engels') == 'Frans':
     print('Bonjour!')
   else
     print('Hello!')
   >Frans of Engels?Frans
```
```python
2. if input('Frans', 'of', 'Engels') = 'Frans':
     print('Bonjour!')
   else:
     print('Hello!')
   >Frans of Engels?Frans
```
```python
3. if input('Frans of Engels') == 'Frans':
   print('Bonjour!')
   else:
     print('Hello!')
   >Frans of Engels?Engels   
```
```python
4. if input('Frans', 'of', 'Engels') = 'Frans':
     print('Bonjour!')
   else:
     print('Hello!')
   >Frans of Engels?Engels
```
```python
5. if input('Frans of Engels') == 'Frans':
     print('Bonjour!)
   else:
     print(Hello!')
   >Frans of Engels?Engels        
```
```python
6. if inputinput('Frans of Engels') == 'Frans':
     print('Bonjour!')
   else:
     print('Hello!')
   >Frans of Engels?Duits  
```
```python
7. if input('Duits', 'of', 'Nederlands') == 'Duits':
   print('Gutenabend!')
   else:
   print('Goedeavond!')
   >Duits of Nederlands?Duits  
```
```python
8. if input('Duits of Nederlands') == 'Duits':
     print('Gutenabend!')
   else
     print('Goedeavond!')
   >Duits of Nederlands?Frans  
```
```python
9. if if input('Duits', 'of', 'Nederlands') == 'Duits':
     print('Gutenabend!')
   else:
   print('Goedeavond!')
     >Duits of Nederlands?Nederlands  
```

 <div style="page-break-after: always;"></div>

2) Foutmeldingen lezen

Je krijgt steeds een foutmelding te zien. Wat is er mis?

```python
1.  if input('melk of suiker?') == 'suiker'                                       ^
    
    SyntaxError: invalid syntax
```

```python
2.  print('gieten')
        ^
    IndentationError: expected an indented block
```

```python
3.  if input('melk of suiker?') = 'suiker':
                                ^
    SyntaxError: invalid syntax
```

```python
4.  if input('melk of suiker?) == 'suiker':
                                        ^
    SyntaxError: invalid syntax
```

   