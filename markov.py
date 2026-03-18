from music21 import converter

from parser import parser
from random import choices


puu, _ = parser()

haettavat, painotus, _ = puu.search([])
viim_haku = [choices(population=haettavat,weights=painotus)[0].key]

kirjasto = {
    0 :"z"  ,
    35:"G," ,
    36:"^G,",
    37:"A," ,
    38:"^A,",
    39:"B," ,
    40:"C"  ,
    41:"^C" ,
    42:"D"  ,
    43:"^D" ,
    44:"E"  ,
    45:"F"  ,
    46:"^F" ,
    47:"G"  ,
    48:"^G" ,
    49:"A"  ,
    50:"^A" ,
    51:"B"  ,
    52:"c"  ,
    53:"^c" ,
    54:"d"  ,
    55:"^d" ,
    56:"e"  ,
    57:"f"  ,
    58:"^f" ,
    59:"g"  ,
    60:"^g" ,
    61:"a"  ,
    62:"^a" ,
    63:"b"  ,
    64:"c'" ,
    65:"^c'",
    66:"d'" ,
    67:"^d'"
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