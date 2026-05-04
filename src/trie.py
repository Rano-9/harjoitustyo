class TrieNode():

    # yhteen nodeen tallennettaan kuinka usein nodessa käyty, muut nodet ja mikä avain oli kun node lisättiin
    def __init__(self,key):
        self.freq = 0
        self.nodes = dict()
        self.note = key
        self.end = False
        self.iter = 0

    def __contains__(self, item):
        nodes = self.nodes
        for i in item:
            try:
                nodes = nodes[i].nodes
            except KeyError:
                return False
        return True


class Trie():

    def __init__(self):
        self.root = TrieNode("root")
        self.uniikkia = set()


    def __contains__(self,item):
        return item in self.root
    
    def insert(self,keys):
        current = self.root
        for i in keys:
            try:
                if current.nodes[i.note]:
                    current = current.nodes[i.note]
                    current.freq +=1

            except KeyError:
                new_node = TrieNode(i.note)
                current.nodes[i.note] = new_node
                current = new_node
                current.freq += 1
                
                self.uniikkia.add(i.note)
                
        current.end = True

    def search(self,keys):
        current = self.root
        for i in keys:
            if hasattr(i,"__dict__"):
                
                try:
                    current = current.nodes[i.note]
                    
                except KeyError:# pragma: no cover
                    
                    return [], [], current
            else: # pragma: no cover

                try:
                    current = current.nodes[i]
                    
                except KeyError:
                    
                    return [], [], current

        freq = []
        nodes = []

        for i in current.nodes.values():
            nodes.append(i)
            freq.append(i.freq)
        return nodes, freq, current
