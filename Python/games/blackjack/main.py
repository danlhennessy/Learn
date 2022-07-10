import random

class card:
    def __init__(self,  type):
        self.type = type
        
    def dealCard():
        card = random.choice(list(cardtypes.keys()))
        print(card)
        
class club(card):
    def __init__(self, type):
        super().__init__(type)
class spade(card):
    def __init__(self, type):
        super().__init__(type)
class diamond(card):
    def __init__(self, type):
        super().__init__(type)
class heart(card):
    def __init__(self, type):
        super().__init__(type)
        
cardtypes = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": [1, 11]}


    
