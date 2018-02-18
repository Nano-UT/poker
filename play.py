from player import *
class game(player):
    def __init__(self,names,btn,sb,bb):
        self._names = names
        self._btn = btn
        self._sb = sb
        self._bb = bb
        self._players = []

    def mkplayers(self):
        for s in self._mnames:
            self._players.append(player(s,"1$"))

    def play(self,players):
        pack = deck()
        pack.shaffle()
        self.mkplayers(names)
        for person in range(len(self._players)):
            person.set(board,[test._deck[0],test._deck[1]])
            del(pack[:2])
        board = pack[:5]
        for tmp in board:
            tmp.turn()
        print(board)




        btn = (btn + 1) % len(self._players)

    def bet(players):
        pass
