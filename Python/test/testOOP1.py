class myString(str):
    def __init__(self, string):
        self.string = string
        super().__init__()
    def append(self, a):
        self.string += a
        return self.string

    def pop(self, p):
        return self.string[:-p]
    
testring = myString("Hellos")

print(testring.pop(1))