class myString(str):
    def __init__(self, string):
        self.string = string
        super().__init__()
        
    def append(self, a):
        self.string += a
        return self.string

    def pop(self, p):
        return self.string[:-p]
    
    def __getitem__(self, index):
        print(f'getting item at index {index}...')
        return self.string[index]
    
    def __setitem__(self, index, value):
        print(f'Changing index {index} from {self.string[index]} to {value}')
        self.string[index] = value
    
testring = myString("Hellos")

print(testring.pop(3))
print(testring)
print(testring[2])

testring[2] = 'a'

print(testring)