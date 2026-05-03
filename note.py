from random import randint

class Note:
    def __init__(self,key,measure=None,length="1/8"):
        self.note = key
        self.measure = measure
        self.length = length

class Tahti():
    def __init__(self):
        self.length = 0
        self.notes = []
        self.last = []
        self.writable = False

    def lisää(self,note_unit,satunnais=False):
        note = note_unit
        pituus = 1
        if satunnais:
            pituus = randint(1,4)
        self.length += float(pituus)
        self.notes.append((note.note, float(pituus)))

        if self.length >= 4:
            self.writable = True


    def kirjoita(self,line,kirjasto):
        tahdin_pituus = 4
        old_line = ""
        viim_nuotti = ()
        for k, v in self.notes:
            tahdin_pituus -= v
            # 1 - 2
            if tahdin_pituus >= 0:
                if v.is_integer():
                    line += f"{kirjasto[int(k)]}{int(v)} "
                    
                else:
                    ratio = v.as_integer_ratio()[1]
                    line += f"{kirjasto[int(k)]}/{int(ratio)} "

            else:

                line +=f"{kirjasto[int(k)]}{int(v+tahdin_pituus)}-"
                old_line = line
                line = "| "
                viim_nuotti = (k,float(abs(tahdin_pituus)))

        self.length = abs(tahdin_pituus)
        if self.length < 4:
            self.writable = False

        self.notes.clear()
        if viim_nuotti:
            self.notes.append(viim_nuotti)

        if "0" in line or "0" in old_line:
            breakpoint()
        return line, old_line
    