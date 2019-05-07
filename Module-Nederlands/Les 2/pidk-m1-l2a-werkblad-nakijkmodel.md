## Les 2: werkblad a nakijkmodel

### Even opfrissen!

1)

De laatste regel print `Goedemorgen`. Hieronder wordt uitgelegd wat fout is aan de andere regels.

1. Mist de ronde haakjes open en sluit en mist de aanhalingstekens.
2. Er wordt een combinatie gemaakt van een enkele en een dubbele aanhalingsteken. Hier moet een keuze in gemaakt worden.
3. De enkele aanhalingstekens om het woord Goedemorgen zijn vergeten
4. Er wordt een combinatie gemaakt van een enkele en een dubbele aanhalingsteken. Hier moet een keuze in gemaakt worden.

2)

1. ```python
   print('Python', 'is', 'een', 'programmeertaal')
   ```

   De bovenste regel is de juiste code. Hieronder wordt uitgelegd wat fout is aan de andere regels.

   2. De aanhalingstekens om `is` en `een` missen. 

   3. Er mist een komma tussen `'een'` en `'programmeertaal'`

   4. De ronde haakjes open en sluit missen, alle aanhalingstekens om alle woorden en de komma tussen al deze woorden met aanhalingstekens missen.

   5. Alle aanhalingstekens om alle woorden de komma tussen al deze woorden met aanhalingstekens missen.

3)

   ```python
   print('Python', 'is', 'een', 'programmeertaal')
   ```

4)

   ```python
   print('Is', 'Het', 'al', 'pauze')
   ```

 <div style="page-break-after: always;"></div>

### Onder elkaar

1) 

1. `Hallo allemaal`

2. `Hallo`

   `Allemaal`

3. **FOUT**
   allemaal mist de aanhalingstekens, dit is nu een niet gedefinieerde variabele in plaats van een string. Over variabele gaat het volgende les. Je krijgt nu een Name error.

4. `Hallo`

   `allemaal`

   Let op het verschil met 2. Daar is Allemaal met een hoofdletter A, hier met een kleine letter a.

5. `Hallo Allemaal`

   Deze code geeft geen fout, maar dit is niet hoe we het de leerlingen leren. 
   Sommige leerlingen zullen denken dat deze code een foutmelding geeft omdat de aanhalingsteken na Hallo, de komma en daarna de aanhalingsteken voor Allemaal mist. Feitelijk gezien kan een computer deze code echter wel lezen: ook een spatie ziet de computer als een karakter. Hij leest nu dus letterlijk Hallo[spatie]Allemaal en print dit. We willen echter voor nu de standaard aanhouden dat de leerlingen alle woorden scheiden zoals bij 1 het geval is. 
6. **FOUT**
   prit is twee keer fout geschreven, de n mist. 

2) 

```python
print(goedemorgen)                              
# FOUT
```

```python
print('Goedemorgen')                            
# Goedemorgen
```

```python
print('goedemorgen')                            
# goedemorgen
```
 <div style="page-break-after: always;"></div>

### Commentaar! 

1) 
Je gebruikt commentaar om:
- Bovenaan te schrijven wat een programma doet
- Uitleg bij een stukje code te geven 
- Een regel code eventjes 'uit' te zetten

2) 

1. 

```python
print('Hallo')                            
# print('Hallo')                        
print('Hallo')  
```

`Hallo`
`Hallo`

De middelste regel wordt niet uitgeprint. Dit is commentaar en python slaat commentaar over.

2. 

```python
# Hallo
print('Hallo')
```

`Hallo`

De eerste regel wordt niet uitgeprint. Dit is commentaar en python slaat commentaar over.

3. 

```python
print(#Hallo)   
```

Deze code geeft een fout. Er wordt een comment geschreven in de functie print(). 
Dit kan niet. Als je hier een comment achter had willen schrijven, dan had je 
`print('Hallo') #Hallo` moeten doen. 

 <div style="page-break-after: always;"></div>

3) 

1. `Goedemorgen`

   De onderste regel wordt niet uitgeprint. Dit is commentaar en python slaat commentaar over.

2. `Hallo kinderen!`
   De bovenste regel wordt niet uitgeprint. Dit is commentaar en python slaat commentaar over.
   
2. `Hallo kinderen!`
   De bovenste regel wordt niet uitgeprint. Dit is commentaar en python slaat commentaar over.
   