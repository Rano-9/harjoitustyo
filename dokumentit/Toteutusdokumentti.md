# Testausdokumentti

### Ohjelman yleisrakenne

Ohjelma tuottaa markovin ketjuilla generoitua musiikkia. 

Harjoitusdatana on käytetty yli 700 kappaletta jotka ovat transponoitu C säveleen. Data on syötetty Trie tietorakenteeseen.

### Aika ja tilavaatimus

Tietorakenteen muodostaminen kestää noin 0.56 sekunttia harjoitusdatasta. 

Kappaleiden luomiseen menevää aikaa testaatiin luomalla tuhat kappaletta. 

Ensin luotiin kymmenellä tahdilla, aikaa kului kokonaisuudessaan 0,76 sekunttia ja keskimäärin 0,0007 sekunttia per kappale. 

Sadalla tahdilla, aikaa kesti kokonaisuudessaan 5,08 sekunttia ja keskimäärin 0,005 sekunttia. 

Tuhannella tahdilla aikaa kesti kokonaisuudessan 31,59 sekunttia ja keskimäärin 0.03 sekunttia. 

Kymmenellä tuhannella tahdilla aikaa kesti kokonaisuudessaan 244,83 sekunttia ja keskimäärin 0,24 

Ja kun luotiin yksi kappale sadalla tuhannella tahdilla kesti siinä aikaa 28,38 sekunttia.

Algoritmin aikavaatimus on .. ...

Midien generoiminen kestää pidempään ja tähän ohjelamssa ei voida vaikuttaa.

### Puutteet ja parannusehdotukset

Ohjelmassa ei toteutuksen puolesta ole puutteita. 

Parannusehdotuksena ohjelma voisi käyttää toisenlaista tietorakenneta kappaleiden kirjoittamiseen. Kun ohjelmalla yritettiin kirjoitaa miljoona tahtia ei se koskaan valmistunut. Tässä todennäköisesti tulee vastaan ohjelman tekninen ongelma. 

Jokainen kappale kirjoitetaan yhdelle string riville rivivaihtoineen ja tämä ei ole loppujen lopuksi kätevä vaihtoehto kun mennään pitkiin riveihin. Tämän voi selittää myös yllättävän hypyn kymmenen ja sadan tuhannen kappaleiden kirjoitus nopeudessa.

### Laajojen kielimallien käyttö

Ohjelman luomisessa tai dokumentoinnissa ei ole käytetty laajoja kielimalleja.

### Käytetyt lähteet

[Trie wikipedia artikkeli](https://en.wikipedia.org/wiki/Trie)

Medium artikkeli: [Markov chain from scratch](https://medium.com/@jdwittenauer/markov-chains-from-scratch-33340ba6535b)