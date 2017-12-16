from hand import num, suit, card, deck, hand, pocketboard

class player(pocketboard):
    def __init__(self, name, board, pocket, stack):
        pobo = board + pocket
        self._player = pocketboard(pobo)
        self._pocket = pocket
        self._fald = False
        self._stack = stack
        self._name = name

    def __repr__(self):
        return "{}\n[{}\033[40m \033[0m{}] {}]".format(self._name, self._pocket[0], self._pocket[1], self._player)

    def stack_lose(self,money):
        self._stack -= money

    def stack_win(self,money):
        self._stack += money
