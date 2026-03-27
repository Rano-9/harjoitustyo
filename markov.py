# pylint ei osaa lataa music21
from music21 import converter # pylint: disable= import-error

import glob
from parser import parser
from random import choices

files = glob.glob("data/kappaleet/Harjoitukset_C_asteikolla/*.abc")
print(files)
puu, _ = parser(files)

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
    75:"^d'"
}
with open("data/demo.abc","w") as file:
    file.write(
"""X: 1
T: demo from markov
M: 4/4
L: 1/8
Q:1/4=60
K:C
V:1
""")
    line = "| "
    viim_viim =[]
    for i in range(-7,93):
        if i % 8 == 0: 
            file.write(f"{line} | \n")
            line = ""
        line += kirjasto[viim_haku[-1]] +" "
        haettavat,painotus,nuotti = puu.search(viim_haku)
        if nuotti is None:

            # tapaus jossa saatiin 0 osumaa. Palataan yksi askel taakse ja lasketaan uusi nuotti
            haettavat,painotus,nuotti = puu.search(viim_viim[:2])
            
            # Jos kävi niin, että kaksi kertaa 0 osumaa, huonotuuri harjoitusmateriaalia liian vähän lopetetaan.
            if nuotti is None:
                print("Lopetettu aikaisin")
                break
            
        viim_haku.append(choices(population=haettavat,weights=painotus)[0].key)
        if len(viim_haku) == 3:
            viim_viim = viim_haku
            viim_haku = viim_haku[1:]


score = converter.parseFile("data/demo.abc",format="ABC")

score.write("midi", fp="data/demo.mid")