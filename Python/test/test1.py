
class testminus:
    def __init__(self, name):
        self.name = name
    def __neg__(self):
        return 45
        
test1 = testminus('John')
one = -test1
print(one)