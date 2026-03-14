class note:
    def __init__(self,key):
        self.note = key

    def __str__(self):
        return self.note[:1]


    def __eq__(self, value):
        if isinstance(value,str):
            return self.note[:1] == value
        return self.note == value.note.note
        

class notes:
    def __init__(self):
        self.notes = []
    
    def insert(self, key):
        self.notes.append(key)


    def __str__(self):
        line = ""
        for n in self.notes:
            line += str(n)
        return line
    

if __name__ == "__main__":

    # käsin testausta että note == note toimii
    test1 = note("g/2")
    test2 = note("G/2")
    test3 = note("g")
    test4 = note("G")

    test5 = note("B2")

    print(str(test5) == "B")
    print(test5)
    print(test1 == test3)
    print(test1 == test2)
    print(test2 == test4)
    print(test3 == test4)