from hand import num, suit, card, deck, hand, pocketboard

class player(HandBoard):
    def __init__(self,pocket,board):
        pobo = pocket + board
        self = pobo
