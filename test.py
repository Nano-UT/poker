from hand import num, suit, card, deck, hand, pocketboard

test = deck()

for x in range(20):
  test.shuffle()
  seven = [test._deck[0],test._deck[1], test._deck[2], test._deck[3], test._deck[4], test._deck[5], test._deck[6]]
  print(seven)
  print(pocketboard(seven))
