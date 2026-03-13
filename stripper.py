from trie import Trie
from note import note, notes
import glob



def stripper():
    puu = Trie()
    muut = []
    for i in r"CDEFGABcdfgabz":
        muut.append(note(i))
    puu.insert(muut)

    
    
    
    files = glob.glob("data/kappaleet/*.abc")
    print(files)
    for f in files:
        alustus = dict()
        alustettu = False
        nuotit = []
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
                for i, v in enumerate(l):
                    if v in "CDEFGABcdefgabz":
                        if i+1 < len(l) and l[i+1] in ("0123456789"):
                            nuotit.append(note(l[i:i+2]))
                        elif i+2 < len(l) and l[i+1] == "/" and l[i+2] in ("0123456789"):
                            nuotit.append(note(l[i:i+3]))
                        else:
                            nuotit.append(note(v))
    

        

        for i in range(len(nuotit)):
            puu.insert(nuotit[i:])

    return puu, alustus

if __name__ == "__main__":
    puusta = stripper()