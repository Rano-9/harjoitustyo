# pylint ei osaa lataa music21
from music21 import converter, instrument, midi # pylint: disable= import-error

import glob
from parser import Parser
from random import choices

from note import Tahti




kirjasto = {
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
class Markov():
    def __init__(self):
        
        self.file = """X: 1
T: demo from markov
M: 4/4
L: 1/8
Q: 1/4=120
K: C
V: 1
"""
        directories = glob.glob("data/kappaleet/*.abc")
        print(f"ladattu: {len(directories)} kappaletta")
        self.depth = 3
        parsija = Parser(self.depth)
        self.puu, _ = parsija.parser(directories)

        haettavat, painotus, _ = self.puu.search([])

        self.viim_haku = [choices(population=haettavat,weights=painotus)[0].key]

        self.peruutuksia = 0
        self.tauot = 0
        self.tahti = Tahti()
        self.viim_viim = []

    def tuota_ketju(self):
        i = 0
        tahteja = 0
        line = "| "
        while True:
            if i == 50:
                break

            self.tahti.lisää(self.viim_haku[-1])

            while self.tahti.writable:
                line, old_line = self.tahti.kirjoita(line,kirjasto)
                if old_line:
                    self.file += old_line
                else:
                    self.file += line
                    line = "| "
                i += 1
                tahteja += 1
            if tahteja == 6:
                self.file += "|\n"
                tahteja = 0
            haettavat,painotus,nuotti = self.puu.search(self.viim_haku)

            if haettavat is None:
                # tapaus jossa saatiin 0 osumaa. Haetaan uusi nuotti viimeisen saadun nuotin mukaan
                haettavat,painotus,nuotti = self.puu.search(self.viim_haku[-1])

                # Jos kävi niin, että kaksi kertaa 0 osumaa, huonotuuri harjoitusmateriaalia liian vähän haetaan juuresta uusi.
                if haettavat is None:
                    haettavat, painotus, _ = self.puu.search([])
                
                self.viim_haku = [choices(population=haettavat,weights=painotus)[0].key]
            
            else:
                self.viim_haku.append(choices(population=haettavat,weights=painotus)[0].key)
            
            if len(self.viim_haku) == self.depth:
                self.viim_viim = self.viim_haku
                self.viim_haku = self.viim_haku[1:]
        

    def kirjoita_ketju(self):
        with open("data/demo.abc","w") as demo:
            for line in self.file:
                demo.write(line)
            demo.close()


def tahdin_kirjoitus(tahti,file,line):
    for x in tahti:
        note, length = x.split(",")
        tahti_pituus += float(length)
        if not float(length).is_integer():
            length = f"/{float(length).as_integer_ratio()[1]}"
        if tahti_pituus <= 4:
            line += kirjasto[int(note)] + length + " "
        else:
            line += kirjasto[int(note)] + str((tahti_pituus - 4))+ "|\n"
            print(line,tahti_pituus,length,tahti_pituus)
            file.write(f"{line}")
            tahti_pituus = tahti_pituus - 4


            if not tahti_pituus.is_integer():
                line += "| " + kirjasto[int(note)] + "/" + str(tahti_pituus.as_integer_ratio()[1]) + " "

            else:
                line += "| " + kirjasto[int(note)] + "/" + str(int(tahti_pituus)) + " "


if __name__ == "__main__":
    ketju = Markov()
    ketju.tuota_ketju()
    ketju.kirjoita_ketju()

    score = converter.parse("data/demo.abc",format="ABC")
    score.write("midi", fp="data/demo.midi")