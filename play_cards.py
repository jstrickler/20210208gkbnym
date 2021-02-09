from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Eliza")
d2 = CardDeck("Henry")
print(d1)

d1.shuffle()
# CardDeck.shuffle(d1)

d2.shuffle()
# CardDeck.shuffle(d2)

for i in range(5):
    print(d1.draw())

cards = d1.get_cards()
print(cards)
print()
print(d1.cards) # CardDeck.cards(...)

print(d1.dealer, d2.dealer)  # call getter

d1.dealer = "Freddie"  #  call setter
print(d1.dealer)

try:
    d1.dealer = [1, 2, 3]
except Exception as err:
    print(err)
else:
    print(d1.dealer)

print(d1.get_ranks())
print(CardDeck.get_ranks())
print()
j1 = JokerDeck("Albert")
print(j1)
j1.shuffle()
print(j1.cards)
print(d1, d2, j1)
# print(str(d1), sep, str(d2), sep, str(j1), end)
print(len(d1), len(d2), len(j1))

print("\U0001F92F")




