import glob

# Käydään läpi sävelmiä jotka ovat yhdessä tiedostossa. Jaetaan "Kirjan" sävelmät harjoitus kansioihin.

directory = glob.glob("data/kirjat/*.abc")
print(directory)
def main(dir):
    kappaleet = 0
    dic = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0,
        "F" : 0,
        "G" : 0

    }
    for f in dir:
        with open(f,"r") as tiedosto:
            rivit = tiedosto.read().splitlines()
        
        lopetukset = 0
        poisto = False
        lopetus = False
        kappale = False
        uusi_rivi = ""
        file = None
        for i, rivi in enumerate(rivit):
            if rivi.startswith("X:"):
                kappaleet += 1
                file = open(f"data/kappaleet/kappale{str(kappaleet)}.abc", "w")
                lopetus = False
                file.write(rivi +"\n")

            elif rivi == "" and rivit[i+1:i+2] == [""] and not lopetus or rivit[i+1:i+2] == [] and file is not None:
                lopetukset += 1
                lopetus = True
                kappale = False
                file = file.close()
            elif rivit[i+1:i+2] == []:
                pass

            elif rivi == "" and rivit[i+1:i+2][0].startswith("X:") and not lopetus and file is not None:
                lopetukset += 1
                lopetus = True
                kappale = False
                file = file.close()
            elif rivi.startswith("L:"):
                file.write(rivi + "\n")
            elif rivi.startswith("M:"):
                file.write(rivi + "\n")

            elif not lopetus and rivi.startswith("K:"):
                dic[rivi[2]] += 1
                kappale = True
                file.write(rivi + "\n")
            
            elif kappale:
                if rivi.startswith("R:"):
                   pass
                elif rivi.startswith("T:"):
                    pass
                elif rivi.startswith("P:"):
                    pass
                elif rivi.startswith("Z:"):
                    pass
                elif rivi.startswith("O:"):
                    pass
                elif rivi.startswith("Q:"):
                    pass
                elif rivi.startswith("C:"):
                    pass
                elif rivi.startswith("%"):
                    pass
                else:
                    for l, k in enumerate(rivi):
                        if k == "\"" and not poisto :
                            poisto = True
                        elif k == "\"":
                            poisto = False
                        elif not poisto:
                            uusi_rivi += k
                    rivit[i] = uusi_rivi
                    uusi_rivi = ""
                    file.write(f"{rivit[i]}\n")
            
            if file is None:
                pass
                

    return kappaleet, lopetukset, dic

print(main(directory))