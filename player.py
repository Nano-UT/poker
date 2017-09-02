from hand import num, suit, card, deck, hand, pocketboard

class player(pocketboard):
    def __init__(self,pocket,board):
        pobo = pocket + board
        self._player = pobo

    def __repr__(self):
        return "{}".format(self._player)

class players(player,n):
    def __init__(self):
        self._fald = []
        for i in range(n):
            self._fald.append(False)
