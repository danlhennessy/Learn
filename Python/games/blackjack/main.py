import random
from deck import deck
from card import card
from player import player


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
        self.player.curval += curcard.value
        while self.player.curval < 21:
            choice = self.player.turn()
            if choice.lower == "stick":
                print(f"Your score is {self.curval}")
            if choice.lower() == "twist":
                curcard = self.deck.drawcard()
                curcard.showcard()
                self.player.curval += curcard.value
                self.player.showval()
        if self.player.curval == 21:
            print("BlackJack!!!")
        if self.player.curval > 21:
            print("Bust!")




if __name__ == '__main__':
    game = blackjack()
    game.run()
