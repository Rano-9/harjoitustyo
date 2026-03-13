from stripper import stripper
from random import choice

file = open("data/demo.abc","w")
node = None
puu, alustus = stripper()

file.write("X: 1 \n")
file.write("T: demo from markov \n")
file.write(alustus["M"] + "\n")
file.write(alustus["L"] + "\n")
file.write(alustus["Q"] + "\n")
file.write(alustus["K"] + "\n")
file.write(alustus["V"] + "\n")

for i in range(100):
    key, node = puu.next(node)
    if i % 4 == 0:
        file.write("\n")
    if key is None:
        key, node = puu.next(None)
        file.write(key.note)
    else:
        file.write(key.note)
