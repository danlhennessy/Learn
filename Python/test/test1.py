class my_container():
    def __init__(self, values):
        self.values = values
    def __len__(self):
        return len(self.values)
        
obj = my_container([1,2,3,4,5])

print(len(obj))