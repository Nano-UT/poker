from hand import num, suit, card, deck, hand, pocketboard
from player import player

def winner(players):
    win = [players[0]]
    for i in range(1,len(members)):
        for x in range(0,6):
            if members[i]._fald == True:
                
