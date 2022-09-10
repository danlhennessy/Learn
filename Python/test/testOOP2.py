class point:
    def __init__(self, x=0, y=0):
        self.move(x, y)
        
    def move(self, x, y):
        self.x = x
        self.y = y