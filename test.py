from hand import num, suit, card, deck, hand, pocketboard
from player import player
from winner import winner

for x in range(20):
  test = deck()
  test.shuffle()
  board = [test._deck[0],test._deck[1], test._deck[2], test._deck[3], test._deck[4]]
  Alice = player("Alice", board, [test._deck[5], test._deck[6]])
  Bob = player("Bob", board, [test._deck[7], test._deck[8]])
  headswinner = winner([Alice,Bob])
  print("Board:", board)
  print(Alice)
  print(Bob)
  print(headswinner,"\n")
