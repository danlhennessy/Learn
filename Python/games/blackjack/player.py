class player:  # player attributes, player turn, draw, showhand
    
    def __init__(self, curval):
        self.curval = curval

    def turn(self):
        return input("Stick or Twist: ")
        
    def showval(self):
        print(self.curval)
    
    def draw(self):
        pass
            
