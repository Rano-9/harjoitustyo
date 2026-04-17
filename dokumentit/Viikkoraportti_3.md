# 3. Viikon raportti

### Mitä olen tehnyt tällä viikolla?

Luotu testejä, niiden edustavuus materiaalista ei ole vielä hyvä. Transponoija luotu ja aloin kehittämään ketjun luomista. Tavoitteena on, että ketju luo kahden edeltävän nuotti parin perusteella seuraavan nuotti parin. Nykyinen malli edustaa paljon toistoa joka on yleistä harjoituskappaleissa.

Eli jono CAEFCCDAEFB tuottais nuotti parit
CA AE EF FC CC CD DA AE EF FB

Tavoitteena olisi nähdä vähenisikö itsestään toistuvat nuotti generaatiot esimerkiksi CCCC. Kun C -> C siirtymien yleisyys vähinisi.

### Miten ohjelma on edistynyt?

Nytten pystyy ottamaan vastaan muita kuin C sävellajin harjoitusdataa ja transponoi. Testaus tehty nyt vain D sävellajilla, kehitetään testausta. Kompastusta tullut harjoitusdatan kohdalla. Harjoitusdataa pitäisi lisätä niin todennäköisyys törmätä ketjuun jolle ei ole jatkoa vähenee. 

Ohjelma ratkaisee tämän lisäämällä täyden tauon ja aloittaa ketjun alusta. Nytten generoidussa musiikissa on 

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Ei selkeää vaikeutta, hitautta aiheuttaa testaus. Ja onko testit edustavia. Testaus on nyt keskittynyt parsijaan eikä markovin ketjuun. Onko mahdollista testata markovin ketjua?

Käytetty aikaa 9 tuntia.