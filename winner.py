from hand import num, suit, card, deck, hand, pocketboard
from player import player

class winner(player):
    def __init__(self,members):
        win = []
        for i in range(0,len(members)):
            if members[i]._fald == False:
                if len(win) == 0:
                    win.append(members[i])
                else:
                    for x in range(6):
                        if members[i]._player._hand._power[x] > win[0]._player._hand._power[x]:
                            win = [members[i]]
                            break
                        elif members[i]._player._hand._power[x] < win[0]._player._hand._power[x]:
                            break
                        elif x == 5:
                            win.append(members[i])
        self._winner = []
        for i in range(0,len(win)):
            self._winner.append(win[i]._name)

    def __repr__(self):
        return "winner:{}".format(self._winner)
