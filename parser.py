from trie import Trie
import glob



def parser():
    puu = Trie()
    ## The 12 Notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B.
    kirjasto = {
    "Ga":35,
    "yGa":36,
    "Aa":37,
    "yAa":38,
    "Ba":39,
    "C":40,
    "yC":41,
    "D":42,
    "yD":43,
    "E":44,
    "F":45,
    "yF":46,
    "G":47,
    "yG":48,
    "A":49,
    "yA":50,
    "B":51,
    "c":52,
    "yc":53,
    "d":54,
    "yd":55,
    "e":56,
    "f":57,
    "yf":58,
    "g":59,
    "yg":60,
    "a":61,
    "ya":62,
    "b":63,
    "cy":64,
    "ycy":65,
    "dy":66,
    "ydy":67,
    "z":0
}

    
    files = glob.glob("data/kappaleet/Harjoitukset_C_asteikolla/*.abc")
    print(files)
    kaikki= []
    for f in files:
        nuotit = []
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
                nuotti = 0
                for i,v in enumerate(rivi):
                
                    if v in "CDEFGABcdefgabz":
                        
                        nuotti += kirjasto[v]
                        if  i+1 < len(rivi)-1:
                            if rivi[i+1] in ",'":
                                if rivi[i+1] == ",":
                                    nuotti += 1
                                else:
                                    nuotti -= 1
                            nuotit.append(nuotti)
                        nuotti = 0

                    elif v in "_^":
                        if v == "^":
                            nuotti += 1
                        else:
                            nuotti -= 1
        
        kolmikot = []
        for i, v in enumerate(nuotit):
            kolmikot.append(nuotit[i:i+3])

        for x in kolmikot:
            if len(x) == 3:
                puu.insert(x)
        kaikki.append(kolmikot)

    return puu, kaikki

if __name__ == "__main__":
    puusta = parser()