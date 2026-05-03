# pylint ei osaa lataa music21
from music21 import converter # pylint: disable= import-error

import glob
from parser import Parser
from random import choices

from note import Tahti





class Markov():
    def __init__(self,depth,directories = None):
        self.file = ""
        self.kirjasto = {
            2 :"z"  ,
            43:"G," ,
            44:"^G,",
            45:"A," ,
            46:"^A,",
            47:"B," ,
            48:"C"  ,
            49:"^C" ,
            50:"D"  ,
            51:"^D" ,
            52:"E"  ,
            53:"F"  ,
            54:"^F" ,
            55:"G"  ,
            56:"^G" ,
            57:"A"  ,
            58:"^A" ,
            59:"B"  ,
            60:"c"  ,
            61:"^c" ,
            62:"d"  ,
            63:"^d" ,
            64:"e"  ,
            65:"f"  ,
            66:"^f" ,
            67:"g"  ,
            68:"^g" ,
            69:"a"  ,
            70:"^a" ,
            71:"b"  ,
            72:"c'" ,
            73:"^c'",
            74:"d'" ,
            75:"^d'",
            76:"e'",
            77:"f'",
            78:"^f'",
            79:"g'",
            80:"^g'"
        }
        if not directories:
            directories = glob.glob("data/kappaleet/*.abc")
            print(f"ladattu: {len(directories)} kappaletta")
        
        self.depth = depth
        parsija = Parser(self.depth)
        self.puu, _ = parsija.parser(directories)
        self.viim_haku = []
        self.peruutuksia = 0
        self.tauot = 0
        self.tahti = Tahti()

    def tuota_ketju(self,index=0,pituus=4,satunnais=False):

        self.file = f"""X: {index}
T: Markovi ketjulla tehtyä musiikkia
M: 4/4
L: 1/8
Q: 1/4=120
K: C
V: 1
"""
        count = 0
        tahteja = 0
        line = "| "
        while True:
            if count == pituus:
                break
            
            haettavat,painotus,nuotti = self.puu.search(self.viim_haku)

            if not haettavat:
                tiputus = 0
                while True:
                    tiputus += 1
                    # tapaus jossa saatiin 0 osumaa. Tiputetaan hakua yhdellä niin kauan,
                    # että löytyy uusi nuotti. Tässä tapauksessa tiputetaan ensimmäinen nuotti

                    self.viim_haku = self.viim_haku[1:]
                    haettavat,painotus,nuotti = self.puu.search(self.viim_haku)
                    
                    if haettavat and painotus:
                        self.viim_haku.append(choices(population=haettavat,weights=painotus)[0])
                        break
                    
                print("Tiputettiin ketjun hakua:",tiputus,"kertaa")
            else:
                self.viim_haku.append(choices(population=haettavat,weights=painotus)[0])

            
            self.tahti.lisää(self.viim_haku[-1],satunnais)

            if len(self.viim_haku) == self.depth:
                self.viim_haku = self.viim_haku[1:]

            while self.tahti.writable:
                line, old_line = self.tahti.kirjoita(line,self.kirjasto)
                if old_line:
                    self.file += old_line
                else:
                    self.file += line
                    line = "| "
                count += 1
                tahteja += 1

            if tahteja == 6:
                self.file += "|\n"
                tahteja = 0
            

            

        if __name__ == "__main__":
            self.kirjoita_ketju(index)
            return None
        else:
            print("Ketjua ei kirjoitettu tiedostoon")
            return self.file

    def kirjoita_ketju(self,index):
        with open(f"data/demo{index}.abc","w") as demo:
            for line in self.file:
                demo.write(line)
            demo.close()

if __name__ == "__main__":
    kertaa = 1
    syvyys = 3
    pituus = 50
    SATUNNAIS = False

    print("Kuinka monta kappaletta haluat (default 1)")
    try:
        kertaa = int(input())

    except ValueError:
        pass
    print("Minkä kertaisen markovin ketju tehdään (default 3)")

    try:
        syvyys = int(input())
        
    except ValueError:
        pass
    print("Kuinka monta tahtia haluat (default 50)")
    
    try:
        pituus = int(input())    
    
    except ValueError:
        pass
    print("satunnaistetaakon tahteja y/n (default Ei)")
    
    SATUNNAIS = input()
    if SATUNNAIS.lower() in ("y","n"):
        if SATUNNAIS == "y":
            SATUNNAIS = True
        else:
            SATUNNAIS = False
    else:
        SATUNNAIS = False
    
    if syvyys > 0:
        ketju = Markov(syvyys)
    else:
        ketju = None


    if ketju:
        for i in range(kertaa):

            ketju.tuota_ketju(i,pituus,SATUNNAIS)

            score = converter.parse(f"data/demo{i}.abc",format="ABC")
            score.write("midi", fp=f"data/demo{i}.midi")
