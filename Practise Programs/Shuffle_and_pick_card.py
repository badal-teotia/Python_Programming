# WAP to shuffle deck of cards and pick 3 of them.

import itertools, random

cards = list(itertools.product(range(1,14),['diamond','spade','heart','club']))
random.shuffle(cards)

print(cards)

for i in range(1,4):
    print(cards[i][0],'of',cards[i][1])
    