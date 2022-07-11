import random
from card import card

cardtypes = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 1}
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

class deck:
    # deck attributes
    def __init__(self):
        self.cards = []
    
    def buildDeck(self):
        for key, value in cardtypes.items():
            self.cards.append(card(suits[0], key, value))
            self.cards.append(card(suits[1], key, value))
            self.cards.append(card(suits[2], key, value))
            self.cards.append(card(suits[3], key, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
        return(self.cards)
    
    def drawcard(self):
        newcard = self.cards.pop()
        return newcard
    
    def showdeck(self):
        for v in self.cards:
            v.showcard()
            
mydeck = deck()

mydeck.buildDeck()  # Builds list of card objects