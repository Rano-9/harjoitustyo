# pylint ei osaa lataa music21
from music21 import converter, instrument, midi # pylint: disable= import-error

import glob
from parser import Parser
from random import choices

directories = glob.glob("data/kappaleet/*.abc")
print(f"ladattu: {len(directories)} kappaletta")
depth = 6
parsija = Parser(depth)
puu, _ = parsija.parser(directories)

haettavat, painotus, _ = puu.search([])

viim_haku = [choices(population=haettavat,weights=painotus)[0].key]

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
    79:"g'"
}


with open("data/demo.abc","w") as file:
    file.write(
"""X: 1
T: demo from markov
M: 4/4
L: 1/8
Q: 1/4=120
K: C
V: 1
""")
    peruutuksia = 0
    tauot = 0
    tahti = []
    line = "| "
    viim_viim =[]
    i = 0
    while True:
        if i == 50:
            break
        tahti.append(viim_haku[-1])

        if len(tahti) == 4:
            for x in tahti:
                line += kirjasto[x] + " "
            file.write(f"{line}|\n")
            line = "| "
            i += 1
            tahti.clear()
                       
        haettavat,painotus,nuotti = puu.search(viim_haku)

        if nuotti is None:

            # tapaus jossa saatiin 0 osumaa. Palataan yksi askel taakse ja lasketaan uusi nuotti
            haettavat,painotus,nuotti = puu.search(viim_viim[:2])
            peruutuksia += 1
            
            # Jos kävi niin, että kaksi kertaa 0 osumaa, huonotuuri harjoitusmateriaalia liian vähän lopetetaan.
            if nuotti is None:
                #lisätään nuottiin kohta joka ilmaisee että katkesi
                
                tauot += 1
                for i in range(4-len(tahti)):
                    line += "z "
                tahti.clear()
                file.write(f"{line}|\n")
                line = "| z4 |"
                file.write(f"{line}\n")
                line = "| "
                i += 2

                #aloitetaan rootista
                haettavat, painotus, _ = puu.search([])
                viim_haku = [choices(population=haettavat,weights=painotus)[0].key]
            
        viim_haku.append(choices(population=haettavat,weights=painotus)[0].key)
        if len(viim_haku) == depth:
            viim_viim = viim_haku
            viim_haku = viim_haku[1:]

print("Lisättyjä taukoja:",tauot)
print("Perrutettu:",peruutuksia,"kertaa")


cl = instrument.Clarinet()

score = converter.parse("data/demo.abc",format="ABC")
score.insert(0,cl)
mf = midi.translate.streamToMidiFile(score)

cl.autoAssignMidiChannel([])
score.write("midi", fp="data/demo.midi")