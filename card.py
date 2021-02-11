class Card:
    def __init__(self, suit, rank, is_trump=False):
        self.suit = suit
        self.value = rank
        self.is_trump = is_trump

    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    # def show(self):
    #     suits = ['JACK', 'QUEEN', 'KING', 'ACE']
    #
    #     if 6 <= self.value <= 10:
    #         rank = str(self.value)
    #     elif 10 < self.value <= 14:
    #         rank = suits[self.value - 11]
    #     else:
    #         print("Invalid rank identifier")
    #     return "{} of {}".format(rank, self.suit)
    def show(self):
        if self.value == 14:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)



