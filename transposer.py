# Transponoidaan kaikki musiikki C avaimeen 

erotus = {
        "C" : 0 ,
        "Fb": 0 ,
        "D" : 2 ,
        "Eb":-2 ,
        "E" : 4 ,
        "Db":-4 ,
        "F" : 6 ,
        "Cb":-6 ,
        "G" : 8 ,
        "Bb":-8 ,
        "A" : 10,
        "Ab":-10,
        "B" : 12,
        "Gb":-12
    }
def transpose(note,key):
    if note == 2:
        return note
    return note + erotus[key]

def check_key(key):

    if key in erotus.keys():
        return True
    print("Key failed",key)
    return False