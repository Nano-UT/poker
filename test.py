from hand import num, suit, card, deck, hand, pocketboard
from player import player
from winner import winner

def mkplayers(names,players):
    for s in names:
        players.append(player(s,board,[test._deck[0],test._deck[1]],"1$"))
        del(test._deck[:2])

class board(card):
    def __init__(self,cards):
        pass

class table(player):
    def __init__(self,players):
        cards = deck()
        cards.shuffle()
        board = [test._deck[0],test._deck[1], test._deck[2], test._deck[3], test._deck[4]]
        pass

playernames = ["Alice","Bob","Charley","Desmond","Emily"]

for x in range(20):
  test = deck()
  test.shuffle()
  board  = [test._deck[0],test._deck[1], test._deck[2], test._deck[3], test._deck[4]]
  del(test._deck[:5])
  players = []
  mkplayers(playernames,players)
  win = winner(players)
  print("Board:", board)
  for t in players:
      print(t)
  print(win,"\033[0m\n")
