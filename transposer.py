# Transponoidaan kaikki musiikki C avaimeen 

erotus = {
    "c am gmix ddor ephr flyd bloc" : 0 ,
    "d bm bmin amix edor f#phr glyd c#loc" : 2 ,
    "b g#m f#mix c#dor d#phr elyd a#loc":-2 ,
    "e c#m bmix f#dor g#phr alyd d#loc" : 4 ,
    "ab fm ebmix bbdor cphr dblyd gloc":-4 ,
    "f dm cmix gdor aphr bblyd eloc" : 6 ,
    "gb ebm dbmix abdor bbphr cblyd floc":-6 ,
    "g em dmix ador bphr clyd f#loc" : 8 ,
    "f# d#m c#mix g#dor a#phr blyd e#loc":-8,
    "a f#m emix bdor c#phr dlyd g#loc" : 10,
    }

def transpose(note,key):
    return note
    if note == 2:

        return note
    for i in erotus.keys():
        if key.lower() in i:
            return (note + erotus[i])
        
    print("ei ollut",key)
    return note

def check_key(key):

    if key in erotus.keys():
        return True
    print("Key failed",key)
    return False