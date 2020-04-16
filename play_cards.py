#!/usr/bin/env python
"""
A main script to play cards
"""
from carddeck import CardDeck, other_method
from jokerdeck import JokerDeck

cd1 = CardDeck("Marisol")
print(cd1)

print(cd1.dealer)

cd1.shuffle()

# cd1._make_deck()  # naughty!
# print(CardDeck.RANKS)

for _ in range(7):
    print(cd1.draw())

try:
    cd1.dealer = 47  # setter property
except TypeError as err:
    print(err)
# same as
# CardDeck.dealer(47)  # wrong!!

print(cd1.dealer)   # getter property

#  getter/setter methods
# cd1.get_dealer()
# cd1.set_dealer(47)

print(cd1.cards)

print(cd1.get_ranks())

print(CardDeck.get_ranks())

CardDeck.say_hello()
other_method()

print(dir(CardDeck))
print()

cd2 = CardDeck("Miranda")

j1 = JokerDeck("Alicia")
print(j1)
j1.shuffle()
print(j1.cards)
print()

j1.strategy()

print(JokerDeck.mro())

j1.wombat()

print(len(cd1))
print(len(cd2))
print(len(j1))  # j1.__len__()
# print(j1.__len__())  wrong

print(cd1)  # print(str(cd1))
print(j1)

print(repr(cd1))

# str(x) human-friendly x
# repr(x) code-friendly x

mega_deck = cd1 + cd2 + j1
print(mega_deck)
mega_deck.shuffle()

d1 = CardDeck("Bob")
d2 = CardDeck("Bob")

print(d1 == d2)
print(d1 == cd1)






