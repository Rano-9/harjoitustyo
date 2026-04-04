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

    def parser(self,files):

        ## The 12 Notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B.
        kaikki= []
        for f in files:
            key = None
            measure = None
            length = None
            done = False
            change = 0
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
                        print("Löytyi avain",key,f)
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
                        next = True

                if length is None or measure is None or key is None or next:
                    pass    
                else:
                    if nuotti != 0:
                        change = transpose(nuotti,key)
                        nuotit.append(Note(change))
                        nuotti = 0
            
                    for i,v in enumerate(rivi):
                        if v == "|":
                            nuotti = 0
                            change = 0
                        #Vaihdetaan avainta kun esiintyy uusi avain nuoteissa
                        if v == "[" and rivi[i+1] == "K":
                            key = rivi[i+3]

                        elif v == "[" and rivi[i+1] == "M":
                            measure = rivi[i+3:i+6]

                        if v in "ABCDEFGabcdefg":
                            nuotti = Note(transpose(self.kirjasto[v],key),measure)

                            osoitin = rivi[i-1]
                            if osoitin in "_^":
                                if osoitin == "_":
                                    nuotti.note -= 1
                                else: 
                                    nuotti.note += 1
                            
                            osoitin = rivi[i+1]

                            if osoitin in ",'":
                                if osoitin == ",":
                                    nuotti.note -= 12
                                else:
                                    nuotti.note += 12

                            if nuotti.note >= 72:
                                osoitin = rivi[i+2]

                                if osoitin in "1234567890":
                                    nuotti.length = osoitin
                                elif osoitin == "/" and rivi[i+3] in "1234567890":
                                    nuotti.length = rivi[i+2:i+4]
                            else:
                                if osoitin in "1234567890":
                                    nuotti.length = osoitin
                                elif osoitin == "/" and rivi[i+2] in "1234567890":
                                    nuotti.length = rivi[i+1:i+3]
                            nuotit.append(nuotti)


#                        #Katsotaan onko ylennyksiä tai alennuksia
#                        elif v in "_^":
#
#                            #Alennetaan tai ylennetään yhdellä
#                            if v == "_":
#                                nuotti -= 1
#                            else:
#                                nuotti += 1
#                            
#                        #Katsotaan mikänuotti kyseessä
#                        elif v in "cdefgabCDEFGABz":
#                            nuotti += self.kirjasto[v]
#            
#                        #Katsotaan oliko se ylä vai ala rekisterissä
#                        elif v in ",'":
#
#                            if v == ",":
#                                nuotti -= 12
#                            else:
#                                nuotti += 12
#
#                        #Katsotaan kuinka pitkään soitetaan
#                        #Jos soitetaan puolet annetusta pituudesta
#                        elif v in "/" and rivi[i+1] in "1234567890" and not done:
#                            nuotit[-1].length = rivi[i:i+2]
#                            done = True
#
#                        elif v in "1234567890" and not done and nuotti != 0:
#                            #Lisätään viimeisimpään lisättyyn nuottiin kesto
#                            breakpoint()
#                            nuotit[-1].length = v
#                            done = True
#
#                        #Merkitään nuotti -3 jotta voidaan välttyä tupla nuoteilta
#
#                        #Katsotaan onko seuraava merkki nuotti
#                        #yritetään välttää index erroria
#                        try:
#                            seuraava = rivi[i+1]
#                        except IndexError:
#                            seuraava = ""
#                        if seuraava in "cdefgabCDEFGABz_^|" and nuotti != 0:
#                            #Jos nuotti, tahtiviiva, ylennys tai alennus kirjataan nykyinen nuotti
#                            change = transpose(nuotti,key)
#                            nuotit.append(Note(change))
#                            if change < 43 and change != 2:
#                                print("Lisätty outo nuotti",change,nuotti,key)
#                            nuotti = 0
#                            done = False
#
#                        if nuotti < 43 and nuotti != 2 and nuotti != 0 and nuotti != -3:
#                            print(rivi,nuotti)
#                        if change < 43 and change != 2 and change != 0 and change != -3:
#                            print(rivi,nuotti,change,v,i )


            syvyys = []
            for i, v in enumerate(nuotit):
                syvyys.append(nuotit[i:i+self.depth])

            for x in syvyys:
                if len(x) == self.depth:
                    self.puu.insert(x)
            kaikki.append(syvyys)

        return self.puu, kaikki

if __name__ == "__main__":
    files = glob.glob("data/kappaleet/Harjoitukset_C_asteikolla/*.abc")
    parsija = Parser()
    puusta = parsija.parser(files)