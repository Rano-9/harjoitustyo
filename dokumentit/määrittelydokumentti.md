# Harjoitustyö Algoritmit ja Tekoäly

Harjoitustyö on tehty pythonilla. 

Opiskelen tietojenkäsittelyn kandilinjalla

Hallinnoin hyvin vain pythonia, ymmärrän muita kielejä pienissä määrin.

### Musiikin generoiminen markovin ketjuilla

Tavoitteena muodostaa musiikki generaattori. Generaattorin ydin on tuottaa musiikkia joka kuulostaa muusiikilta, hyödyntäen markovin ketjuja. Sovellus mahdolliesti transponoi tuotettun musiikki ja annetun harjoitusdatan. Generoitu musiikki on abc notaationa ja kuuneltavissa midinä. (mahdollisesti generoitu musiikki luettavissa nuotistona).

Generointiin käytetään markovin ketjuja ja harjoitusdata trie-tietorankenteessa. 

Sovellukseen voi itse syöttää harjoitusdataa tai hyödyntää valmista harjoitussettiä. Harjoitusdata koostuu abc notaatiolla koostetuista nuoteista.  

Minkä ongelman ratkaiset?

    Ratkaisen miten generoida satunnaista, mutta musiikilta kuulostavia tuotoksia.

### Tavoitteena olevat aika- ja tilavaativuudet (esim. O-analyysit)

    Tästä kannattaa selvittää niin paljon kuin voitte. Ei ole tarkoitus todistaa tai mitata mitään itse.

    Trie wikipedian mukaan on O(n). Markovin ketjujen aikavaativuus on riippuvainen sekoittumisesta ja vaihtelee O(nlog(n)) ja O(n²) välillä

    Käytä aika ja tilavaatimuuksia apuvälineenä ymmärtääksenne, miten työhön kannattaa asennoitua.

        Nämä kannattaa katsoa wikipediasta ja varmistaa, että ymmärrätte oman algoritmin kohdalla mistä ne tulevat. Miksi algoritmisi tarvitsee sen verran aikaa?

### Lähteet, joita aiot käyttää.

    Wikipedia
