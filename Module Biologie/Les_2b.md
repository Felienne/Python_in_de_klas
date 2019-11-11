### Laat de muis stuiteren

Deze opdracht wordt afgetekend als:

- De muis over het scherm beweegt, van boven naar beneden
- Jij in je schrift hebt uitgelegd hoe het stuiteren werkt

**Uitleg**
Zorg dat de muis niet meer uit beeld verdwijnt, maar aan de onder- **en bovenrand** van het veld omdraait. In de les heb je deze code gezien:

```python
    if muis_rechthoek.bottom > 600:
        # draai om
        print("de muis draait om!")
        snelheid_muis = [0, -1]
```

Voeg deze code aan je eigen programma toe in de `while True:`

Zorg nu dat de muis ook aan de bovenrand omdraait. Kijk daarvoor goed bij welke waarde de muis bovenaan is. Kopieer dan de code met de if en pas die aan. Je code ziet er dan zo uit:

```python
while True:   #<-- dit staat al in de code! dat hoef je dus niet nog eens te typen
    #hier staat alle code voor het bewegen die je al hebt

    if muis_rechthoek.bottom > 600:
        # draai om
        print("de muis draait om!")
        snelheid_muis = [0, -1]
    if .... #<- maak deze code zelf af!
```

### Laat de leeuw stuiteren

Deze opdracht wordt afgetekend als:

- Je in je schrift hebt geschreven welke regels over de muis gaan (alleen de nummers)
- De leeuw over het scherm beweegt, van links naar rechts
- Je per regel opschrijft wat je denkt dat de regel doet

**Uitleg**
Kijk eens goed welke regels er nu allemaal over de muis gaan. Schrijf die nummers in je schrift.

Zorg dat de leeuw niet meer uit beeld verdwijnt, maar aan de rechter- **en linkerrand** van het veld omdraait. Kijk naar de code van de muis, en gebruik dezelfde soort code voor de leeuw.

**Belangrijk:** Gebruik voor de leeuw `leeuw_rechthoek.right` en niet bottom want de leeuw stuitert van links naar recht en we moeten dus kijken of de rechterkant de rand raakt.

### Laad je eigen plaatjes in

Deze opdracht wordt afgetekend als:

- Je je eigen dierenplaatjes gebt gezocht en ingeladen in je simulatie
- Je de namen van de variabele netjes hebt aangepast naar jouw roofdier en prooidier.

**Uitleg**
Vorige week heb je zelf twee dieren gekozen. Zoek nu op internet goede plaatjes op van die dieren. 

**Let op!** Je mag plaatjes niet zomaar pakken. 

Denk aan de Google-regels van mevr. Hermans en stel je zoekresultaten in via Tools - Usage Rights - Labeled for reuse. 

Upload de plaatjes naar je simulatie en pas de code aan zodat die plaatjes worden ingeladen. 

Pas ook de variabelenamen aan! Het is niet netjes als er `muis_rechthoek` in jouw code staat, staat terwijl je bijv. een antilope inlaadt. Daar kun je van in de war raken. 

###Stuiter door het veld (extra)

Deze opdracht wordt afgetekend als:

- De muis en de leeuw schuin bewegen
- De muis en de leeuw allebei aan alle vier de randen stuiteren

**Uitleg**
De muis en de leeuw stuiteren nu allebei maar een richting op, eentje links-rechts en eentje omhoog-omlaag. Maar ze kunnen ook schuin door het veld. Maak de snelheid dan bijv. [1,2] en [2,1]. 

Nu stuiteren ze niet helemaal goed want de muis loopt links en rechts het veld uit, en de leeuw juist boven en onder. Kan jij dat repareren?

###Begin op een willekeurige plek (extra)

Deze opdracht wordt afgetekend als:

- De muis en de leeuw niet linksboven maar op een willekeurige plek beginnen

**Uitleg**
Ieder plaatje begint standaard links bovenin, maar dat kun je ook aanpassen. Denk aan deze vragen om je te helpen:

* Welke waardes meot je denk je aanpassen om de plaats van de muis en leeuw in te stellen?
* Weet je nog hoe je een willekeurige waarde kiest? 