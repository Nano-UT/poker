from hand import num, suit, card, deck, hand, pocketboard
from player import player

test = deck()
test.shuffle()
board  = [test._deck[0],test._deck[1], test._deck[2], test._deck[3], test._deck[4]]
del(test._deck[:5])
Arith = player("Arith",board,[test._deck[0],test._deck[1]],10000)
Arith.action(1,2)
