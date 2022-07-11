import random


cardtypes = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": [1, 11]}
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
class card:
    
    def __init__(self):
        pass
        
    def dealCard(self):
        card = random.choice(list(cardtypes.keys()))
        print(card) #Type of card
        print(cardtypes[card]) #Value of card
        
class club(card):
    suit = "Hearts"
    def __init__(self):
        super().__init__()
class spade(card):
    suit = "Hearts"
    def __init__(self):
        super().__init__()
class diamond(card):
    suit = "Hearts"
    def __init__(self):
        super().__init__()
class heart(card):
    suit = "Hearts"
    def __init__(self):
        super().__init__()
        


card1 = card()

card1.dealCard()