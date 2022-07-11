class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
    def Area(self):
        return self.length * self.width
    
    def display(self):
        print(self.width, self.length, self.Perimeter(), self.Area())
        
    
myrect = rectangle(5, 10)

myrect.display()


class Parallelepipede(rectangle):
    def __init__(self, length, width, height):
        self.height = height
        super().__init__(length, width)
    
    def Volume(self):
        return (self.height * self.width * self.length)

    
mypara = Parallelepipede(10, 12, 10)

print(mypara.Volume())