from hand import num, suit, card, deck, hand, pocketboard

class player(pocketboard):
    def __init__(self, board, pocket):
        pobo = board + pocket
        self._player = pocketboard(pobo)
        self._pocket = pocket
        self._fald = False

    def __repr__(self):
        return "{},{}".format(self._pocket,self._player)

class players(player):
    def __init__(self, ):
