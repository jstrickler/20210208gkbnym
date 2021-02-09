import random

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # tuple
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def get_cards(self):  #getter method BAD (or so)
        return self._cards

    @property
    def cards(self):  # getter property
        return self._cards

    @property
    def dealer(self):  # getter property
        return self._dealer.upper()

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    def __len__(self):  # responds to global function len()
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer}, {len(self)})"