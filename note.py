class Note:
    def __init__(self,key,measure=None):
        self.note = key
        self.measure = measure
        self.length = None

    def __str__(self):
        return self.note[:1]


    def __eq__(self, value):
        if isinstance(value,str):
            return self.note[:1] == value
        return self.note == value.note.note
        

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