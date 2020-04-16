#!/usr/bin/env python
from carddeck import CardDeck

class Game:
    def strategy(self):
        print("strategizing...")


class JokerDeck(Game, CardDeck):

    def _make_deck(self):
        super()._make_deck()
        for joker_num in "1", "2":
            card = joker_num, "Joker"
            self._cards.append(card)
