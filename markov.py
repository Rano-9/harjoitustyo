from stripper import stripper
from random import choices

file = open("data/demo.abc","w")
puu, _ = stripper()

haettavat, painotus, _ = puu.search([])
viim_haku = [choices(population=haettavat,weights=painotus)[0].key]

kirjasto = {
    52:"a" ,
    53:"b" ,
    47:"c" ,
    48:"d" ,
    49:"e" ,
    50:"f" ,
    51:"g" ,
    0: "z" ,
    45:"A" ,
    46:"B" ,
    40:"C" ,
    41:"D" ,
    42:"E" ,
    43:"F" ,
    44:"G"
}

file.write("""
X: 1
T: demo from markov
M: 4/4
L: 1/8
Q:1/4=120
K: Bmin
V:1
""")
line = "|"
for i in range(100):
    if i % 8 == 0: 
        file.write(f"{line}\n")
        line = ""
    line += kirjasto[viim_haku[-1]] +" "
    haettavat,painotus,nuotti = puu.search(viim_haku)
    if nuotti is None:
        break
    viim_haku.append(choices(population=haettavat,weights=painotus)[0].key)
    if len(viim_haku) == 3:
        viim_haku = viim_haku[1:]