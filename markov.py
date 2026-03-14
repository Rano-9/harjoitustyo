from stripper import stripper
from random import choice

file = open("data/demo.abc","w")
node = None
puu, alustus = stripper()

file.write("""
    X: 1 \n
    T: demo from markov \n 
    M: 9/8 \n
    L: 1/8 \n
    Q:1/4=120 \n
    K: Bmin \n
    V:1 \n
    |
""")

for i in range(100):
    key, node = puu.next(node)
    if i % 4 == 0:
        file.write("\n")
    if key is None:
        key, node = puu.next(None)
        file.write(key.note)
    else:
        file.write(key.note)
