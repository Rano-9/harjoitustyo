from note import Notes

class TrieNode():

    # yhteen nodeen tallennettaan kuinka usein nodessa käyty, muut nodet ja mikä avain oli kun node lisättiin
    def __init__(self,key):
        self.freq = 0
        self.nodes = dict()
        self.key = key
        self.end = False

    def __eq__(self, value):
        return self.key == value

    def __str__(self):
        if isinstance((self.key),int):
            return str(self.key)
        string = ""
        for i in self.key:
            string += " " + str(i)
        return string

class Trie():

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self,keys):
        current = self.root
        for i in keys:
            if isinstance(i,list):
                try:
                    if current.nodes[i[0]]:
                        current = current.nodes[i[0]]
                        current.freq +=1

                except KeyError:
                    new_node = TrieNode(Notes(i))
                    current.nodes[i[0]] = new_node
                    current = new_node
                    current.freq += 1
            else:
                try:
                    if current.nodes[i.note]:
                        current = current.nodes[i.note]
                        current.freq +=1

                except KeyError:
                    new_node = TrieNode(i.note)
                    current.nodes[i.note] = new_node
                    current = new_node
                    current.freq += 1
        current.end = True

    def search(self,keys):
        current = self.root
        for i in keys:
            
            try:
                current = current.nodes[i]
                
            except KeyError:
                
                return None, None, None
            
        freq = []
        nodes = []

        for i in current.nodes.values():
            nodes.append(i)
            freq.append(i.freq)
        return nodes, freq, current.key
