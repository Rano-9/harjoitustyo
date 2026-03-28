import unittest
from trie import Trie, TrieNode
from parser import Parser
from os import path

class TestParser(unittest.TestCase):
    
    def setUp(self):
        self.file = ["tests/data/mock.abc"]
        self.parsija = Parser()
        self.result, _ = self.parsija.parser(self.file)

    
    def test_Parser(self):

        # Testaan parserin lopputulosta. Pitäisi olla Trie olio
        self.assertIsInstance(self.result, Trie)
        self.assertIsInstance(self.result.root, TrieNode)
    
    def test_Trie(self):

        # Testaan että Trie on kolmen noden syvä
        depth = 0
        node = list(self.result.root.nodes.values())
        while node:
            depth += 1 
            node = drill(node)

        self.assertEqual(depth,3)

    def test_Trie_sisältää_testi_nuotteja(self):
        # Testi materiaalissa on C' c' D tämä vastaa 60, 72, 50
        # Sekä tärkeä edge case jossa on d', E', e eli 74, 56, 56. ' merkki toimii oudosti.

        file = ["tests/data/mock2.abc"]
        result, _ = self.parsija.parser(file)
        nodes, _, search =  result.search([60])
        
        self.assertEqual(search.key,60)
        self.assertFalse(60 in nodes)
        self.assertTrue(72 in nodes)

        nodes, _, search = result.search([74])

        self.assertEqual(search.key,74)
        self.assertFalse(74 in nodes)
        self.assertTrue(64 in nodes)

        nodes, _, search = result.search([74,64])

        self.assertEqual(search.key,64)
        self.assertFalse(66 in nodes)
        self.assertTrue(64 in nodes)

    def test_parser_löytää_sävellajin(self):
        self.assertIsNotNone(self.parsija.key)

    def test_parser_löytää_muun_kuin_C_sävellajin(self):
        result = self.parsija.parser(["tests/data/mock3.abc"])
        self.assertIsNot(self.parsija.key, "C")
        self.assertIs(self.parsija.key, "D")
    
    def test_parserin_transponoinja_toimii(self):
        result, _ = self.parsija.parser(["tests/data/mock3.abc"])
        self.assertIsNotNone(result.search([62])[2])
        self.assertIsNotNone(result.search([74])[2])

def drill(node):
    node = node[0]
    return list(node.nodes.values())