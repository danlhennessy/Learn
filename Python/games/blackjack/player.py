from deck import deck


class player:  # player attributes, player turn, draw, showhand
    
    def __init__(self, curval):
        self.curval = curval

    def turn(self):
        choice = input("Stick or Twist: ")
        if choice.lower() == "stick":
                print(f"Your score is {self.curval}")
        if choice.lower() == "twist":
            curcard = self.drawcard()
            curcard.showcard()
            self.curval += curcard.value
            print(self.curval)
        else:
            print("You can only Stick or Twist")
            
    def showval(self):
        print(self.curval)
    
    def draw(self):
        pass
            
