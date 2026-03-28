from trie import Trie
from transposer import transpose

import glob

class Parser():
    def __init__(self,depth=3):
        self.kirjasto = {
        "C":48,
        "D":50,
        "E":52,
        "F":53,
        "G":55,
        "A":57,
        "B":59,
        "c":60,
        "d":62,
        "e":64,
        "f":65,
        "g":67,
        "a":69,
        "b":71,
        "z":2
    }
        self.puu = Trie()
        self.key = None
        self.depth = depth

    def parser(self,files):

        ## The 12 Notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B.
        kaikki= []
        for f in files:
            key = None
            nuotit = []
            nuotti = 0
            with open(f,"r") as tiedosto:
                rivit = tiedosto.read().splitlines()

            for rivi in rivit:
                if key is None:
                    if rivi.startswith("K:"):
                        self.key = rivi[2:]
                        self.key = self.key.split(" ")[0]
                        key = self.key

                else:
                    if nuotti != 0:
                        nuotit.append(transpose(nuotti,key))
                        nuotti = 0
            
                    for i,v in enumerate(rivi):
                        if v in "_^":
                            if nuotti != 0:
                                nuotit.append(transpose(nuotti,key))
                                nuotti = 0
                            if v == "_":
                                nuotti -= 1
                            else:
                                nuotti += 1
                            

                        elif v in "cdefgabCDEFGABz":
                            
                            if nuotti != 0 and abs(nuotti) != 1:
                                nuotit.append(transpose(nuotti,key))
                                nuotti = 0
                            nuotti += self.kirjasto[v]

                        elif v in ",'":
                            if v == ",":
                                nuotti -= 12
                            else:
                                nuotti += 12
            nuotit.append(nuotti)

            parit = []
            for i, v in enumerate(nuotit):
                if len(nuotit[i:i+2]) == 2:
                    parit.append(nuotit[i:i+2])
        
            syvyys = []
            for i, v in enumerate(parit):
                syvyys.append(parit[i:i+self.depth])

            for x in syvyys:
                if len(x) == self.depth:
                    self.puu.insert(x)
            kaikki.append(syvyys)

        return self.puu, kaikki

if __name__ == "__main__":
    files = glob.glob("data/kappaleet/Harjoitukset_C_asteikolla/*.abc")
    parsija = Parser()
    puusta = parsija.parser(files)