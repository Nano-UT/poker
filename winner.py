from hand import num, suit, card, deck, hand, pocketboard
from player import player

def winner(players):
    win = players[0]
    for i in range(1,len(players)):
        for x in range(0,6):
            if players[i]._kjfdmekwf[x] > winner._enginj[x]: #playersの仕様決めて
                win = players[i]
