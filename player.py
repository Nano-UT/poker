from hand import num, suit, card, deck, hand, pocketboard

class player(pocketboard):
    def __init__(self, name, board, pocket):
        pobo = board + pocket
        self._player = pocketboard(pobo)
        self._pocket = pocket
        self._fald = False
        self._name = name

    def __repr__(self):
        return "{}:{},{}".format(self._name, self._pocket, self._player)
