# Testaus

Ohjelmaan on luotu kolme automaatio testiä. Testeissä käydään läpi ohjelman tietorakennetta Trieä, parsijan toimintaa ja markovin ketjun generointia. 

Trie testi testaa, että tietorakenteessa on oikean kokoinen syvyys. 

Parsijan testit testaa, että harjoitus data on syötetty oikein tieotrakenteeseen. Tämä käydään luomalla mock datasta halutun ketjun kertaisen kokoisia ryhmiä ja verrataan niitä tieoto rakenteessa olevaan dataan. Jos kaikki ryhmät ovat rakenteessa testi läpäisee. 

Markovin ketjun generaatiota testaan käymällä lävitse generoidun ketjun jokainen pari ja testaan ovatko ne mahdollisia tuotoksia mock datasta. Tämä testi epäonnistuu jos löytyy tuotos joka ei ole ketjussa. 

Testissä on myös huomioitavaa, ettei kata tapauksia jossa on jouduttu aloittamaan ketjun generointi uudestaan. Tähän ei ole vielä ratkaisua kirjoitettu.