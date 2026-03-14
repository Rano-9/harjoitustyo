from trie import Trie
from note import note, notes
import glob



def stripper():
    puu = Trie()
    muu = set()

    
    files = glob.glob("data/kappaleet/*.abc")
    print(files)
    nuotit = []
    for f in files:
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
                for i, v in enumerate(l):
                    if v in "CDEFGABcdefgabz":
                        muu.add(v)
                        if i+1 < len(l) and l[i+1] in ("0123456789"):
                            nuotit.append(note(l[i:i+2]))
                        elif i+2 < len(l) and l[i+1] == "/" and l[i+2] in ("0123456789"):
                            nuotit.append(note(l[i:i+3]))
                        else:
                            nuotit.append(note(v))


            puu.insert([[x[0],x[1]] for x in zip(nuotit[::2], nuotit[1::2])])
            puu.insert([[x[0],x[1],x[2]] for x in zip(nuotit[::2], nuotit[1::2],nuotit[2::3])])
            puu.insert([[x[0],x[1],x[2],x[3]] for x in zip(nuotit[::2], nuotit[1::2],nuotit[2::3],nuotit[3::4])]
    )
    #puu.cycle()
    return puu, nuotit

if __name__ == "__main__":
    puusta = stripper()