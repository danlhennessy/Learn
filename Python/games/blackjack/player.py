class player:  # player attributes, player turn, draw, showhand

    def __init__(self, curval):
        self.curval = curval

    def turn(self, deck):
        while self.curval < 21:
            choice = input("Stick or Twist: ")
            if choice.lower == "stick":
                print(f"Your score is {self.curval}")
            if choice.lower() == "twist":
                curcard = deck.drawcard()
                curcard.showcard()
                self.curval += curcard.value
                self.showval()
        if self.curval == 21:
            print("BlackJack!!!")
        if self.curval > 21:
            print("Bust!")

    def showval(self):
        print(self.curval)
