import unittest
from trie import Trie, TrieNode
from parser import Parser
from os import path

class TestParser(unittest.TestCase):

    def setUp(self):
        self.file = ["tests/data/mock.abc"]
        self.depth = 5
        self.parsija = Parser(self.depth)
        self.result, _ = self.parsija.parser(self.file)
        self.kirjasto = {
            "c": 60,
            "d": 62,
            "e": 64,
            "a": 69,
            "f": 65,
            "g": 67
        }

    def test_Trie(self):

        # Testaan että Trie on annetun syvä
        depth = 0
        node = list(self.result.root.nodes.values())
        while node:
            depth += 1 
            node = drill(node)

        self.assertEqual(depth,self.depth)

    def test_Trie_sisältää_harjoitus_datan(self):

        # Mock data on listattu
        mock = ["f","g","a","e","d","a","e","c",
                "c","d","e","c","d","c","e","d",
                "c","d","a","e","d","a","f","f",
                "d","d","a","e","d","a","f","g"]
        testi_jonot= []
        jono = []

        # Listasta tehdään syvyyden kokoisia pieniä listoja ja käännetään ne numeerisiksi
        for i in range(len(mock)+self.depth-1):
            try:
                jono.append(self.kirjasto[mock[i]])
            except IndexError:
                testi_jonot.append(jono)
                jono = jono[1:]

            if len(jono) == self.depth:
                testi_jonot.append(jono)
                jono = jono[1:]

        # Testataan että jokainen jono uusi jono on Triessä in komennon avulla

        for i in testi_jonot:
            self.assertTrue(i in self.parsija.puu)

        # Testataan, että viimeinen pari on Triessä
        self.assertTrue([65] in self.parsija.puu)

def drill(node):
    node = node[0]
    return list(node.nodes.values())