class TrieNode():

    def __init__(self,key):
        self.freq = 0
        self.nodes = dict()
        self.key = key
        self.end = False

class Trie():

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self,keys):
        current = self.root
        for i in keys:
            try:
                
                if current.nodes[i]:
                    current = current.nodes[i]
                    current.freq +=1

            except KeyError:
                new_node = TrieNode(i)
                current.nodes[i] = new_node
                current = new_node
                current.freq += 1
        current.end = True

    def search(self,key):
        current = self.root
        for i in key:
            try:
                current = current.nodes[i]
            except KeyError:
                return None, None, None
            
        freq = []
        nodes = []

        for i in current.nodes.values():
            nodes.append(i)
            freq.append(i.freq)

        return nodes,freq, current
