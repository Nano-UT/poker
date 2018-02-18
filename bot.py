from hand import *

class bot(pocketboard):
    def __init__(self, name, board, pocket, stack):
        pobo = board + pocket
        self._player = pocketboard(pobo)
        self._pocket = pocket
        self._fald = False
        self._stack = stack
        self._name = name
        self._ai = False

    def __repr__(self):
        return "{}\n[{}\033[40m \033[0m{}] {}]".format(self._name, self._pocket[0], self._pocket[1], self._player)

    def stack_lose(self,money):
        self._stack -= money

    def stack_win(self,money):
        self._stack += money

    def action(self,bet,fbet):
        if self._fald and self._ai:
            return None
        else:
            while(True):
                act = input("Please make action.\n")
                if act[0] in ["a","A"]:
                    self._ai = True
                    break
                elif act[0] in ["r","R"]:
                    vul = input("Raise to ???\n")
                    try:
                        vul = int(vul)
                        if vul > self._stack or vul < (bet * 2 - fbet):
                            print("Raise not enough.\n")
                        else:
                            return(vul,bet)
                    except ValueError:
                        print("Invalid input.\n")
                elif act[0] in ["c","C"]:
                    return betf
                else:
                    print("Invalid input.\n")
