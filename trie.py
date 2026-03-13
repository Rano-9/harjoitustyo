class TrieNode():

    def __init__(self, note=None):
        self.nodes = {}
        self.note = note
        self.isLeaf = False


from random import randint
from random import choice
from note import note, notes

class Trie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self,key):
        curr = self.root
        fail = 0
        
        for c in key:
            avain = str(c)

            try:
                curr = curr.nodes[avain]

            except KeyError:
                fail += 1
                curr.nodes[avain] = TrieNode(c)
                curr = curr.nodes[avain]

        curr.isLeaf = True
    
    def next(self,node:TrieNode = None):

        if node is None:
            curr = self.root
        
        else:
            curr = node
        
        keys = list(curr.nodes.keys())
        try:
                
            key = choice(keys)
            note = curr.nodes[key].note
            return note, curr.nodes[key]
        except IndexError:
            return None, None
        
    def search(self,key):
        
        curr = self.root
        
        
        
        
