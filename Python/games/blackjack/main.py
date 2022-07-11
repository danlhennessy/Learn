import random


cardtypes = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": [1, 11]}
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
class blackjack:
    pass
    #Initialise game, create resources, create loop to run game until 21, deal cards
class player:
    pass
    #player attributes, player turn, draw, showhand, 

class card:
    #card attributes, showcard
    
    def __init__(self, suit, type, value):
        self.suit = suit
        self.type = type
        self.value = value
    
    def showcard(self):
        print(f"{self.type} of {self.suit}")
        
class deck:
    #deck attributes, build deck, shuffle, drawcard, show cards in deck
    def __init__(self):
        cards = []
    
    def buildDeck(self):
        pass
    def shuffle(self):
        pass
    def drawcard(self):
        drawntype = random.choice(list(cardtypes.keys()))
        drawncard = card(random.choice(suits), drawntype, cardtypes[drawntype])
        return drawncard
        
mydeck = deck()
mydeck.drawcard().showcard()







#if __name__ == '__main__':
#    game = blackjack()
#    game.run()