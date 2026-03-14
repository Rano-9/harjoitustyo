from stripper import stripper
from random import choice

file = open("data/demo.abc","w")
puu, _ = stripper()
key = choice(list(puu.root.nodes.keys()))
node = next(iter(puu.root.nodes[key]))
note = node.real

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

    if i % 4 == 0:
        file.write("\n")
    if note is None:
        key = choice(list(puu.root.nodes.keys()))
        node = next(iter(node.nodes[key]))
        note = node.real
    else:
        file.write(node.real)
        if node.end:
            key = choice(list(puu.root.nodes.keys()))
            node = next(iter(puu.root.nodes[key]))
        else:
            key = choice(list(node.nodes.keys()))
            node = next(iter(node.nodes[key]))
