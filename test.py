from hand import num, suit, card, deck, hand, pocketboard
from player import player

for x in range(20):
  test = deck()
  test.shuffle()
  board = [test._deck[0],test._deck[1], test._deck[2], test._deck[3], test._deck[4]]
  Alice = player(board,[test._deck[5], test._deck[6]])
  Bob = player(board,[test._deck[7], test._deck[8]])
  print("Board:", board)
  print("Alice's Pocket:", Alice._pocket, "Alice's Hand:", Alice._player._hand)
  print("Bob's Pocket:", Bob._pocket, "Bob's Hand:", Bob._player._hand)
