class card:     # card attributes, showcard

    def __init__(self, suit, type, value):
        self.suit = suit
        self.type = type
        self.value = value

    def showcard(self):
        print(f"{self.type} of {self.suit}")
