import random


cardtypes = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": [1, 11]}
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


class blackjack:
    # Initialise game, create resources, create loop to run game until 21, deal cards
    pass


class player:
    pass  # player attributes, player turn, draw, showhand


class card:
    # card attributes, showcard   
    def __init__(self, suit, type, value):
        self.suit = suit
        self.type = type
        self.value = value

    def showcard(self):
        print(f"{self.type} of {self.suit}")


class deck:
    # deck attributes, build deck, shuffle, drawcard, show cards in deck
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
        return self.cards.pop()
    
    def showdeck(self):
        for v in self.cards:
            v.showcard()


mydeck = deck()

mydeck.buildDeck()  # Builds list of card objects
mydeck.showdeck()
mydeck.drawcard()
mydeck.showdeck()




# if __name__ == '__main__':
#    game = blackjack()
#    game.run()
