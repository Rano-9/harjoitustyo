from stripper import stripper
from random import choice

file = open("data/demo.abc","w")
puu, _ = stripper()
key = choice(list(puu.root.nodes.keys()))
node = next(iter(puu.root.nodes[key]))
note = node.real

file.write("""
X: 1
T: demo from markov
M: 4/4
L: 1/8
Q:1/4=120
K: Bmin
V:1
""")
file.write("|")
for i in range(100):

    if i % 4 == 0:
        file.write("\n")
    if note is None:
        key = choice(list(puu.root.nodes.values()))
        node = next(iter(key))
        note = node.real
    else:
        file.write(node.real)
        if node.end:
            key = choice(list(puu.root.nodes.values()))
            node = next(iter(key))
            note = node.real
        else:
            key = choice(list(node.nodes.values()))
            node = next(iter(key))
            note = node.real
