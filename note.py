class Note:
    def __init__(self,key,measure=None,length="1/8"):
        self.note = key
        self.measure = measure
        self.length = length
        self.modifiedlength = "1"
        self.key = None

    def __str__(self):
        return self.note[:1]


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
                        self.modifiedlength = f"/{multiplier*denominator}"
                        print(self.length)
                    else:
                        if int(multiplier/denominator) == 1:
                            self.modifiedlength = 1
                        else:
                            self.modifiedlength = f"/{int(multiplier/denominator)}"
                else:
                    if pienempi:
                        self.modifiedlength = f"{int(self.modifiedlength)/multiplier}"
                     
                    else:
                        self.modifiedlength = f"{multiplier*int(self.modifiedlength)}"
            else:
                print("HUPS",self.length,self.modifiedlength)
        self.key = f"{self.note},{self.modifiedlength}"
            



        

class Notes:
    def __init__(self,notes):
        self.notes = notes
        self.last = notes[-1]
    
    def __str__(self):
        line = ""
        for n in self.notes:
            line += " " + str(n)
        return line
    
    def __iter__(self):
        for i in self.notes:
            yield i
    



if __name__ == "__main__":
    pass