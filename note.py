class Note:
    def __init__(self,key,measure=None,length="1/8"):
        self.note = key
        self.measure = measure
        self.length = length
        self.modifiedlength = "1"
        self.key = None

    def __eq__(self, value):
        if isinstance(value,Note):

            

            if self.note == value.note and float(self.modifiedlength) == float(value.modifiedlength):
                return True
            return False
        return False


    def fix(self):
        pienempi = False
        if self.length != "1/8":
            if "/" in self.length:
                fraction = self.length.split("/")
                denominator = int(fraction[1])
                if denominator > 8:
                    multiplier = int(denominator/8)
                    pienempi = True
                else:
                    multiplier = int(8/denominator)


                if "/" in self.modifiedlength:
                    denominator = int(self.modifiedlength.split("/")[1])
                    if pienempi:
                        self.modifiedlength = f"{float(multiplier*denominator)}"
                    else:
                        if int(multiplier/denominator) == 1:
                            self.modifiedlength = 1
                        else:
                            self.modifiedlength = f"{float(multiplier/denominator)}"
                else:
                    if pienempi:
                        self.modifiedlength = f"{int(self.modifiedlength)/multiplier}"
                     
                    else:
                        self.modifiedlength = f"{multiplier*int(self.modifiedlength)}"
            else:
                print("HUPS",self.length,self.modifiedlength)
        elif "/" in self.modifiedlength:

            fraction = self.modifiedlength.split("/")
            self.modifiedlength = 1/int(fraction[1])

        self.key = f"{self.note},{self.modifiedlength}"
            



        

class Tahti():
    def __init__(self):
        self.length = 0
        self.notes = []
        self.last = []
        self.writable = False

    def lisää(self,note_unit):
        note, length = note_unit.split(",")
        self.length += float(length)
        self.notes.append((note, float(length)))

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
    