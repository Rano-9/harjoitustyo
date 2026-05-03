# 7. Viikon raportti

### Mitä olen tehnyt tällä viikolla?

Luotu testejä. Testejä on vain kolme. Yksi testi testaa onko Trie oikein muodostunut eli kuinka syvä on yksi haara. 

Toinen testi käy läpi että harjoitusdata löytyy Triestä pyydetyssä asteessa.
Esimerkiksi jonosta "a b c d a d f f" löytyy kolmannen asteen mukaan jonot "a b c" "b c d" ... .... " a d f" "d f f" sekä "f f" ja "f" myös löytyvät.

Kun ketjun generaatio joutuu näihin tiputtaa se astettansa sitä mukaa kunnes löytää seuraavan nuotin ja joissain tapauksissa aloittaa alusta. 

Kolmas testi käy sitten läpi että generoitu data on ollut harjoitusdatassa. Tämä käy läpi generoidun datan jonot jotka ovat halutun aseteen mukaisia. Ja tarkistaa, että ne ovat Triessä. Tässä oletan myös että Trie oli oikein muodostettu, koska toinen testi läpäisi niin silloin tämäkin testi olisi oikein.
 
Testi ei kuitenkaan tiedä missä kohtaa astetta on tiputettu, ja epäonnistuu vain jos löytyy dataan kuulumaton nuotin. Testi data on myös tarkoituksella tehty sellaiseksi jossa ei ole kohtaa joka johtaa generoinnin jatkamista satunnaisesta nuotista.

### Miten ohjelma on edistynyt?

Ohjelma tuottaa oikeaa tulosta, kuulostaa muusiikilta jonka musiikinteoriasta tietämätön voisi kirjoittaa. Midi konvertointi toimii jolla voi kuunnella musiikkia.. Dokumentaatiota ei ole ja testit ovat rikki. Nämä hoidetaan tulevalla viikolla. Ketjun tuotos on myös satunnaista ja ei kuulosta että seuraisi jotain tiettyä kappaletta.

Käytetty aikaa 7 tuntia.