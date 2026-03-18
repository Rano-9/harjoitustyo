from trie import Trie
from note import note, notes
import glob



def stripper():
    puu = Trie()
    kirjasto = {
    "a" :52,
    "b" :53,
    "c" :47,
    "d" :48,
    "e" :49,
    "f" :50,
    "g" :51,
    "z" :0,
    "A" :45,
    "B" :46,
    "C" :40,
    "D" :41,
    "E" :42,
    "F" :43,
    "G" :44
}

    
    files = glob.glob("data/kappaleet/*.abc")
    print(files)

    for f in files:
        nuotit = []
        alustus = dict()
        alustettu = False
        
        for l in open(f).read().splitlines():
            
            if not alustettu:
                if l.startswith("X:"):
                    pass

                elif l.startswith("T:"):
                    pass

                elif l.startswith("M:"):
                    alustus["M"] = l.strip()
                    
                elif l.startswith("L:"):
                    alustus["L"] = l.strip()
                    
                elif l.startswith("Q:"):
                    alustus["Q"] = l.strip()
                    
                elif l.startswith("K:"):
                    alustus["K"] = l.strip()
                    
                elif l.startswith("V:"):
                    alustus["V"] = l.strip()
                    
                else:
                    alustettu = True
            elif l.startswith("%"):
                pass
            else:
                for v in l:
                    if v in "CDEFGABcdefgabz":
                        nuotit.append(kirjasto[v])
        
        kolmikot = []
        for i, v in enumerate(nuotit):
            kolmikot.append([])
            kolmikot[-1].append(v)
            try:
                kolmikot[-2].append(v)
            except IndexError:
                pass
            try:
                kolmikot[-3].append(v)
            except IndexError:
                pass

        for x in kolmikot:
            if len(x) == 3:
                puu.insert(x)

    return puu, kolmikot

if __name__ == "__main__":
    puusta = stripper()