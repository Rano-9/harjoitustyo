# 1. Viikon raportti

### Mitä olen tehnyt tällä viikolla?
Aloitettu työn tekeminen, saatu aikaiseksi abc notaatiolla olevien kappaleiden käsittely, ja jonkinkaltaista trie rakennelmaa.
### Miten ohjelma on edistynyt?
Ohjelma on ensimmäisessä vaiheessa. Pystyy tekemään jonkinkaltaisen markovin ketjun. Tällä hetkellä ketjujen koko määräytyy jo harjoitusmateriaalin lisäämisessä. **Tämän ei pitäisi näin toimia**
### Mitä opin tällä viikolla / tänään?
Trier tietorakenteet vaikuttavat simppeleiltä, mut en ihan hiffaa miten ne toimii. Mut edistystä on, nykyinen rakenne ei ole viel O(n) tasoa, varsinkin kun lisäämisessä on käytetty muita rakenteita. 

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Trie puut ovat todellisuudessa aiheuttaneet vaikeuksia. Viikon aikana yrittänyt yhtä kappaletta lisätä. Saan sen rakenteeseen, mutta en keksi millään pitäisikö rakenteen olla yksiulotteinen puu kun lisätty yksi merkkijono vai tuleeko yhdestä kappaleesta (merkkijonosta) jo haaroja.

Nykyinen kappaleen parsija (stripper.py) parsi kappaleen nuotit erikseen. Säilyttäen kuitenkin tiedon nuotti luokkaan, onko nuotti puolikas, neljäsosa, kahdeksasosa, vai kuudestoistaosa. 

Parsimisen jälkeen yhdistää nuotit 2, 3, 4 ryhmiin joista ketju käy hakemassa juuresta yhden ketjun käy sen läpi, sen jälkeen valitsee uuden 2, 3, 4 ryhmitetyn ketjun.

Tästä en ole varma käykö tämä markovin ketjuna ja onko trie rakenne oikein.  

Mitä teen seuraavaksi?
