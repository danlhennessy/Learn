import random
from deck import deck
from card import card
from player import player


cardtypes = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 1}  # Fix Ace value later
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


class blackjack:
    def __init__(self):
        self.player = player(0)
        self.deck = deck()
        
    # Initialise game, create resources, create loop to run game until 21, deal cards
    def run(self):
        self.deck.buildDeck()
        self.deck.shuffle()
        curcard = self.deck.drawcard()
        curcard.showcard()
        self.curval += curcard.value
        while self.curval < 21:
            self.player.turn()
            




if __name__ == '__main__':
    game = blackjack()
    game.run()
