import unittest
from trie import Trie, TrieNode
from parser import parser
from os import path

class TestParser(unittest.TestCase):
    
    def setUp(self):
        self.file = ["tests/data/mock.abc"]
        self.result, _ = parser(self.file)
        return super().setUp()
    
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

        self.assertEqual(depth,3,"Test")


def drill(node):
    node = node[0]
    return list(node.nodes.values())