from trie import Trie
from transposer import transpose
from note import Note

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
        self.depth = depth
        self.uuniikit = set()

    def parser(self,files):

        ## The 12 Notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B.
        kaikki= []
        for f in files:
            key = None
            measure = None
            length = None
            skip = ""
            nuotit = []
            nuotti = 0
            next = False
            with open(f,"r") as tiedosto:
                rivit = tiedosto.read().splitlines()

            for rivi in rivit:
                next = False
                if key is None:
                    if rivi.startswith("K:"):

                        key = rivi[2:]
                        key = key.split(" ")[0]
                        next = True
                if measure is None:
                    if rivi.startswith("M:"):
                        measure = rivi[2:]
                        measure = measure.split(" ")[0]
                        next = True
                if length is None:
                    if rivi.startswith("L:"):
                        length = rivi[2:]
                        length = length.split(" ")[0]

                        if length == "":
                            length = rivi[2:]
                            length = length.split(" ")[1]

                        next = True

                if length is None or measure is None or key is None or next:
                    pass
                else:

                    for i,v in enumerate(rivi):
                        if v == "|":
                            nuotti = 0
                        #Vaihdetaan avainta kun esiintyy uusi avain nuoteissa
                        if v == "K":
                            key = rivi[i+2]
                            skip = key

                        elif v == "M":
                            measure = rivi[i+2:i+5]

                        elif v == skip:
                            skip = ""

                        elif v in "ABCDEFGabcdefgz":
                            nuotti = Note(transpose(self.kirjasto[v],key),measure,length)
                            perus = self.kirjasto[v]

                            osoitin = rivi[i-1]
                            if osoitin in "_^":
                                if osoitin == "_":
                                    nuotti.note -= 1
                                    perus -=1
                                else: 
                                    nuotti.note += 1
                                    perus += 1
                            try:
                                osoitin = rivi[i+1]

                                if osoitin in ",'":
                                    if osoitin == ",":
                                        nuotti.note -= 12
                                        perus -= 12
                                    else:
                                        nuotti.note += 12
                                        perus += 12

                                if perus >= 72 or osoitin in ",'":
                                    osoitin = rivi[i+2]

                                    if osoitin in "1234567890":
                                        nuotti.modifiedlength = osoitin

                                    elif osoitin == "/" and rivi[i+3] in "1234567890":
                                        nuotti.modifiedlength = rivi[i+2:i+4]
                                else:
                                    if osoitin in "1234567890":
                                        nuotti.modifiedlength = osoitin


                                    elif osoitin == "/" and rivi[i+2] in "1234567890":
                                        nuotti.modifiedlength = rivi[i+1:i+3]
                            except IndexError:
                                pass
                            self.uuniikit.add(nuotti.note)
                            nuotit.append(nuotti)
                            nuotti = 0

            lisättävät_nuotit = []
            jono = []

            for i in range(len(nuotit) + self.depth-1):

                try:
                    jono.append(nuotit[i])
                except IndexError:
                    lisättävät_nuotit.append(jono)
                    jono = jono[1:]

                if len(jono) == self.depth:
                    lisättävät_nuotit.append(jono)
                    jono = jono[1:]

            for x in lisättävät_nuotit:
                self.puu.insert(x)

        print(len(self.uuniikit),"uniikkia nuottia")
        return self.puu, kaikki

if __name__ == "__main__":
    files = glob.glob("data/kappaleet/Harjoitukset_C_asteikolla/*.abc")
    parsija = Parser()
    puusta = parsija.parser(files)
