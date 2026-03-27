from trie import Trie
import glob



def parser(files):
    puu = Trie()
    ## The 12 Notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B.
    kirjasto = {
    "C":48,
    "D":50,
    "E":52,
    "F":53,
    "G":55,
    "A":57,
    "B":59,
    "c":60,
    "d":62,
    "e":64,
    "f":65,
    "g":67,
    "a":69,
    "b":71,
    "z":2
}

    

    kaikki= []
    for f in files:
        nuotit = []
        nuotti = 0
        alustus = dict()
        alustettu = False
        with open(f,"r") as tiedosto:
            rivit = tiedosto.read().splitlines()

        for rivi in rivit:
            
            if not alustettu:
                if rivi.startswith("X:"):
                    pass

                elif rivi.startswith("T:"):
                    pass

                elif rivi.startswith("M:"):
                    alustus["M"] = rivi.strip()
                    
                elif rivi.startswith("L:"):
                    alustus["L"] = rivi.strip()
                    
                elif rivi.startswith("Q:"):
                    alustus["Q"] = rivi.strip()
                    
                elif rivi.startswith("K:"):
                    alustus["K"] = rivi.strip()
                    
                elif rivi.startswith("V:"):
                    alustus["V"] = rivi.strip()
                    
                else:
                    alustettu = True
            elif rivi.startswith("%"):
                pass
            else:
                if nuotti != 0:
                    nuotit.append(nuotti)
                    nuotti = 0
        
                for i,v in enumerate(rivi):
                    
                    if v in "_^":
                        if nuotti != 0:
                            nuotit.append(nuotti)
                            nuotti = 0
                        if v == "_":
                            nuotti -= 1
                        else:
                            nuotti += 1
                        

                    elif v in "cdefgabCDEFGABz":
                        
                        if nuotti != 0 and abs(nuotti) != 1:
                            nuotit.append(nuotti)
                            nuotti = 0
                        nuotti += kirjasto[v]

                    elif v in ",'":
                        if v == ",":
                            nuotti -= 12
                        else:
                            nuotti += 12
        nuotit.append(nuotti)

        
        kolmikot = []
        for i, v in enumerate(nuotit):
            kolmikot.append(nuotit[i:i+3])

        for x in kolmikot:
            if len(x) == 3:
                puu.insert(x)
        kaikki.append(kolmikot)

    return puu, kaikki

if __name__ == "__main__":
    files = glob.glob("data/kappaleet/Harjoitukset_C_asteikolla/*.abc")
    print(files)
    puusta = parser(files)