class my_container():
    def __init__(self, values):
        self.values = values
    def __len__(self):
        return len(self.values)
        
obj = my_container({1: "one", 2: "two", 3: "tthre"})

print(len(obj))