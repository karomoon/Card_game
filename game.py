from card import Card
from deck import Deck
from player import Player
import random
import collections


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = self.set_players()
        self.trump = None
        self.starting_player_index = 0
        self.leading_card = None  # mast
        self.round_num = 0
        self.cards_played = []  # current tihi
        self.talker = self.players[self.starting_player_index]

    def set_players(self):
        players = [Player()]
        num_of_players = int(input("How many players: "))
        for _ in range(num_of_players):
            name = input("Enter your name: ")
            players.append(Player(name))
            print(len(players))
        return players

    # def get_first_active_player(self):
    #     highest_value = 0
    #     highest_card = None
    #     for player in self.players:
    #         if player.taked == 0:
    #             # card = player.take_card(self.deck.deal())
    #             if player.take_card(self.deck.deal()).value > highest_value:
    #                 highest_card = player.take_card(self.deck.deal())
    #                 highest_value = player.take_card(self.deck.deal()).value
    #         if highest_card in player.hand:
    #             print(f"{player} alustab rääkimist")
    #             return player

    def deal_cards(self, num):
        for _ in range(num):
            for player in self.players:
                player.take_card(self.deck.deal())

    def number_of_rounds(self):
        lst = []
        rounds = len(self.deck.cards) // len(self.players)

        for i in range(1, rounds + 1):
            lst.append(str(i))



        num_of_firsts = list(len(self.players) * lst[0])
        num_of_lasts = list(len(self.players) * lst[-1])
        joined = num_of_firsts + lst[1:-1] + num_of_lasts + lst[-1::-1] + num_of_firsts[:-1]
        joined_ints = [int(i) for i in joined]
        print(joined_ints)
        return joined_ints

    def who_talks(self):
        if self.starting_player_index < len(self.players) - 1:
            self.starting_player_index += 1
        else:
            self.starting_player_index = 0
        return self.starting_player_index

    def round(self):
        self.deck.build()
        self.deck.shuffle()
        if self.round_num == len(self.deck.cards) // len(self.players):
            self.trump = random.choice(self.deck.cards)
            self.deal_cards(self.round_num)
        else:
            self.deal_cards(self.round_num)
            self.trump = self.deck.flip_trump()
        print(f"Trump: {self.trump}")

        overall_guess = 0

        for i in range(len(self.players)):
            player = self.players[(self.starting_player_index + i) % len(self.players)]
            player.show_hand()
            player.make_a_guess()

        for i in range(self.round_num):
            for player in self.players:
                played_card = player.make_move(self.leading_card, self.trump)
                if player == self.talker:
                    print(self.talker)
                    self.leading_card = played_card
                self.cards_played.append(played_card)
                print(player.name + " played " + str(played_card))
            print(self.leading_card)

            highest_value = 0
            highest_card = None

            highest_trump = None
            highest_trump_value = 0

            for card in self.cards_played:
                if card.suit == self.trump and card.value > highest_trump_value:
                    highest_trump = card
                    highest_trump_value = card.value
                elif card.suit == self.leading_card.suit and card.value > highest_value:
                    highest_card = card
                    highest_value = card.value
            print(self.cards_played)
            if highest_trump in self.cards_played:
                taking_player = self.players[(self.cards_played.index(highest_trump))]
            else:
                taking_player = self.players[(self.cards_played.index(highest_card))]
            # taking_player = self.players[self.starting_player_index].hand(highest_card)
            taking_player.taked += 1

            print(taking_player.name + " võttis")
            print(f"{taking_player.name} tihid: {taking_player.taked}")
            self.leading_card = None
            self.talker = self.players[self.players.index(taking_player)]
            self.cards_played = []

        print("\n=== CURRENT STANDINGS ===")
        for player in self.players:
            player.scoring()
            print(f"{player} points: {player.score}")
            player.discard_tihis()
            if player.hand:
                player.hand = []

        self.starting_player_index = self.who_talks()
        self.talker = self.players[self.starting_player_index]
        self.cards_played = []
        self.leading_card = None
        self.deck.discard_trump()

    def game(self):
        # self.starting_player_index = self.players.index(self.get_first_active_player())
        for i in self.number_of_rounds():
            self.round_num = i
            self.round()


if __name__ == "__main__":
    game = Game()
    game.game()

