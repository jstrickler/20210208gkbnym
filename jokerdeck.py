from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _create_deck(self):
        super()._create_deck()  # call _create_deck() in superclass
        for i in 1, 2:
            joker = i, "Joker"
            self._cards.append(joker)

