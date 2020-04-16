import unittest
import sys
from carddeck import CardDeck

class TestCardDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:  # test CASE fixture
        pass

    @classmethod
    def tearDownClass(cls) -> None:  # test CASE fixture
        pass

    def setUp(self):  # test fixture
        self.test_deck = CardDeck("TEST USER")

    @unittest.skipUnless(sys.platform == 'win32', "Only implemented on Windows")
    def test_deck_has_52_cards(self):
        self.assertEqual(52, len(self.test_deck), "Deck does not have 52 cards")

    def test_deck_has_all_combos(self):
        for rank in CardDeck.RANKS:
            for suit in CardDeck.SUITS:
                card = rank, suit
                self.assertIn(card, self.test_deck._cards, f"Card {card} not in deck")

    def test_drawing_card_decrements_deck(self):
        len_before = len(self.test_deck)
        self.test_deck.draw()
        len_after = len(self.test_deck)
        self.assertEqual(len_before -1, len_after, "Drawing card does not decrement deck")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
