from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.trump = Card(None, None)
        self.build()

    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(6, 15):
                self.cards.append(Card(suit, val))
        self.shuffle()

    def shuffle(self):
        return random.shuffle(self.cards)

    def show(self):
        for card in self.cards:
            print(card.show())

    def flip_trump(self):
        self.trump = self.cards.pop()
        return self.trump.suit

    def discard_trump(self):
        self.trump = Card(None, None)

    def deal(self):
        return self.cards.pop()


