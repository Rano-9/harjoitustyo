class TrieNode():

    def __init__(self, note=None):
        self.note = note
        if self.note is not None:
            self.real = note.note
        else:
            self.real = None
        self.nodes = dict()
        self.line = ""
        self.end = False

from note import note
class Trie():

    def __init__(self):
        self.root = TrieNode()
        pass

    def insert(self,key):
        current = self.root
        for i in key:
            current = self.root
            for l in i:
                new_node = TrieNode(l)
                try:
                    current.nodes[str(l)].add(new_node)
                except KeyError:
                    current.nodes[str(l)] = set()
                    current.nodes[str(l)].add(new_node)

                current = new_node
            current.end =True

    def next(self):
        pass