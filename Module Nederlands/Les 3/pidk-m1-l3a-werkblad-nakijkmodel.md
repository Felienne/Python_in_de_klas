<img src="../../img/Logo cs-certificate.jpg" style="zoom:20%" align="right" />

## Les 3 werkblad a nakijkmodel

### Even opfrissen!

1)

1. `Klas 1c` <br/>
  Print goedemorgen wordt niet uitgeprint, deze code is namelijk uitgecomment. Python slaat commentaar over en print dit dus niet uit.

  

2. Hier wordt niets uitgeprint, de eerste regel is commentaar met uitleg over het programma, de tweede regel is commentaar (uitgecommente code).  

    

3. `Hallo allemaal`<br/>
   `Ik ben Python!`<br/>
   De teksten '# je kunt twee woorden printen' en '#maar ook drie' worden niet uitgeprint, dit zijn comments die achter de code zijn geplaatst (een comment begint wanneer je een hekje plaatst).

   

4. `Goedemorgen`

    '# een woord' op dezelfde regels als Goedemorgen wordt <u>niet</u> uitgeprint, dit is een comment die achter de code is geplaatst.
   De tweede regel is ook een comment en wordt dus in zijn geheel niet uitgeprint.

   

5. `Hallo`<br/>
   `klas 1c`<br/>
   De onderste regel wordt niet geprint, dit is uitgecommente code.

2)

1. `prnt` is fout geschreven, moet `print` zijn (de i mist).

    

2. De tweede `print('Allemaal')` staat in de eerste regel code, dit zal een foutmelding veroorzaken. Deze code moet naar de volgende regel

    

3. Er mist een aanhalingsteken voor `allemaal')` .

    

4. De komma tussen `'Hallo'` en `'allemaal'` mist.

    

5. De ronde haakjes missen. Rond haakje open na `print` en rond haakje sluit na `Allemaal'`

    

6. `prit` is fout geschreven, moet `print` zijn (de n mist).

<div style="page-break-after: always;"></div>

### Waardes zoeken

1) 

Er moet een streep getrokken zijn tussen de variabele definitie en het gebruik van de variabele. Voorbeeld:

![afbeelding-1-waardes-zoeken-pidk-m1-l3a-werkblad](/Users/lisa/Github/PidK/Module-Nederlands/Les 3/afbeelding-1-waardes-zoeken-pidk-m1-l3a-werkblad.png)

2)

1. `Hallo allemaal`

    

2. `Hallo 1c`

    

3. `Hallo mevrouw Hermans`

    

4. **Fout**, er staat een komma maar er komt niks achter de komma.

    

5. `Halloleerlingen van klas 1c`
Let op: doordat de komma is vergeten tussen Hallo en leerlingen komt er geen spatie tussen de twee woorden. Python geeft geen foutmelding, maar doet hierdoor niet precies wat wijw ille.

   <div style="page-break-after: always;"></div>

### Naam niet gedefinieerd

1. **Fout**

   De gebruikte variabele `naam` is niet gedefinieerd, en de gedefinieerde variabele `klas` wordt niet gebruikt. Onderstaand is de goede manier:

   ```python
   klas = '1c'
   print('Hallo', klas)
   ```

   of

   ```python
   naam = 'Felienne'
   print('Hallo', naam)
   ```

   

2. `Hallo 1c`

  Code zal geen foutmelding geven, maar in plaats van `'1c'` moet er in de print gebruik gemaakt worden van de gedefinieerde variabele `klas` die als waarde `'1c'` heeft gekregen. Onderstaand is de goede manier:

  ```python
  klas = '1c'
  print('Hallo', klas)
  ```

  

3. **Fout**

   De gebruikte variabele `Hermans` is niet gedefinieerd, en de gedefinieerde variabele `achternaam` wordt niet gebruikt. Let op: Hermans was als gedefinieerde variabele een foutieve variabele geweest, een variabelenaam begin je in python met een kleine letter. Onderstaand is de goede manier:

   ```python
   achternaam = 'Hermans'
   print('Hallo', 'mevrouw', achternaam)
   ```

   

4. `Het is half 9`

   Hier is correct gebruik gemaakt van de variabele tijd_op_klop die als waarde 'half 9' heeft gekregen.

    <div style="page-break-after: always;"></div>

5. `Hallo leerlingen van klas 1c`

   Hier is correct gebruik gemaakt van de variabele klas die als waarde 'klas 1c' heeft gekregen.

    

6. **Fout**

   De gebruikte variabele `Goedemorgen` is niet gedefinieerd.
   In plaats van `Goedemorgen` moet er in de print gebruik gemaakt worden van een gedefinieerde variabele `goedemorgen` die als waarde `'Goedemorgen'` krijgt.
   Let op: Goedemorgen was als gedefinieerde variabele een foutieve variabele geweest, een variabelenaam begin je in python met een kleine letter. 
   Onderstaand is de goede manier:

   ```python
   goedemorgen = 'Goedemorgen'
   print(goedemorgen)
   ```

   

7. `Het is tijd`

  Code zal geen foutmelding geven, maar in plaats van `'tijd'` moet er in de print gebruik gemaakt worden van de gedefinieerde variabele `tijd` . Onderstaand is de goede manier:

  ```python
  tijd = 'half 9'
  print('Het', 'is', tijd)
  ```

  

8. `Goedemorgen` 

   Code zal geen foutmelding geven, maar in plaats van `'Goedemorgen'` moet er in de print gebruik gemaakt worden van een gedefinieerde variabele `goedemorgen` die als waarde `'Goedemorgen'` krijgt.

   Onderstaand is de goede manier:

   ```python
   goedemorgen = 'Goedemorgen'
   print(goedemorgen)
   ```

