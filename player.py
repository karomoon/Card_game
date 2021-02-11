from card import Card
import random


class Player:
    def __init__(self, name="You",  score=0):
        self.name = name
        self.talker = False
        self.score = score
        self.hand = []
        self.guess = 0
        self.taked = 0

    def __str__(self):
        return self.name

    def take_card(self, card):  # kutsuda deal() ajal
        self.hand.append(card)

    def tihis_won(self):
        self.taked += 1

    def discard_tihis(self):  # pärast roundi voetud tihid 0
        self.taked = 0

    def show_hand(self):
        print("{}'s hand: {}".format(self.name, self.hand))
        return self

    def make_a_guess(self):
        guess = int(input("Mitu võtad?: "))
        self.guess = guess

    def scoring(self):
        if self.guess == 0 and self.taked == 0:
            self.score += 10
        elif self.guess == self.taked:
            self.score += 15 * self.taked
        elif self.guess > self.taked:
            self.score -= 15 * (self.guess - self.taked)

        elif self.guess < self.taked:
            self.score += self.taked
        return self.score

    # def make_move(self):
    #     for card in self.hand:
    #         card = int(input("Enter your move: "))
    #         print(f"{self.name} played {card} and it is leading card")
    #         try:
    #             card = self.hand[card]
    #         except:
    #             print("Invalid choice. Try again")
    #
    #         self.hand.remove(card)
    #         return card

    def make_move(self, leading_card, trump):
        possible_cards = []
        if leading_card == None:
            leading_card = Card('NONE', -1)
        if not self.talker:
            for card in self.hand:
                if card.suit == leading_card.suit or card.suit == trump:
                    possible_cards.append(card)
            if not possible_cards:
                for card in self.hand:
                    possible_cards.append(card)
        while True:
            if self.talker:
                print(possible_cards)
                card_choice = int(input("Enter your move >> "))
            else:
                print(possible_cards)
                card_choice = int(input("Enter your move >> "))
            try:
                card = possible_cards[card_choice]
                break
            except:
                print("Invalid choice. Try again")

        self.hand.remove(card)

        return card
