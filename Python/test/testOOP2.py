class point:
    def __init__(self, x=0, y=0):
        """Create a point, if no x or y values are provided, they are set to a default 0"""
        self.move(x, y)
        
    def move(self, x, y):
        """Move the point by provided x and y values"""
        self.x += x
        self.y += y
        
mypoint = point(2,5)

print(mypoint.x, mypoint.y)

mypoint.move(12, 29)

print(mypoint.x, mypoint.y)
