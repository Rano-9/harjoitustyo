import unittest
from markov import Markov
from os import path

class TestParser(unittest.TestCase):

    def setUp(self):
        self.file = ["src/tests/data/mock.abc"]
        self.kirjasto = {
            "c": 60,
            "d": 62,
            "e": 64,
            "a": 69,
            "f": 65,
            "g": 67
        }

    def test_markov_ketju_tuottaa_satunnaista_mutta_datassa_olevia_nuotteja(self):
        for i in range(1,6):
            depth = i
            markov = Markov(depth,self.file)

            file = markov.tuota_ketju()

            #Ketjussa on 6 riviä pakollisia ABC tietoja, tiputetaan nämä saadaan generoitu pätkä

            file =file.split("\n")[7:][0]

            #Otetaan tahdit erilleen

            tahdit = file.split("| ")[1:]

            #Luodaan tahdeista erillisiä nuotteja

            testi_nuotit = []
            for i, v in enumerate(tahdit):

                tahdit[i] = tahdit[i].split("1 ")
                for x in tahdit[i]:
                    if x:
                        testi_nuotit.append(x)

            #Laitetaan nuotit jonoon jotka ovat syvyydeltään samoja kuin generoitu syvyys

            jono = []
            testi_jonot = []
            for i in testi_nuotit:
                jono.append(self.kirjasto[i])
                if len(jono) == depth:
                    testi_jonot.append(jono)
                    jono = jono [1:]
            print(file)
            # Testataan jonot. Jono voi sisältää osia jotka eivät ole suoraan harjoitus datasta.
            # Tällöin tiputetaan haettavien määrää yhdellä.
            # Testi epäonnistuu jos on tuotettu asioita joita ei ole koskaan ollut harjoitus datassa
            #
            # Esimerkiksi: harjoitus datassa on pätkä f f joka loppuu aina tilanteeseen
            # jossa aloitetaan generointi 0. asteesta.
            #
            # Testeissä kuitenkin tarkistetaan, että mikään nuotti ei ole datan ulkopuolelta

            mock = ["f","g","a","e","d","a","e","c",
                    "c","d","e","c","d","c","e","d",
                    "c","d","a","e","d","a","f","f",
                    "d","d","a","e","d","a","f","g"]

            mock_jonot = []
            jono.clear()
            for i in range(len(mock)+depth-1):
                try:
                    jono.append(self.kirjasto[mock[i]])
                except IndexError:
                    mock_jonot.append(jono)
                    jono = jono[1:]

                if len(jono) == depth:
                    mock_jonot.append(jono)
                    jono = jono[1:]

            for i in testi_jonot:
                self.assertIn(i,mock_jonot)

            # Lopuksi testataan yhdistelmiä jota ei voi olla datasta:

            self.assertFalse([60,69] in markov.puu)
            self.assertFalse([65,65,60] in markov.puu)
