import math
import random

mode = True

class num:

  def __init__(self, num):
      if mode:
        number = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
      else:
        number = ["dews", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King", "Ace"]
      self._num = number[(num + 11) % 13]
      self._size = (num + 11) % 13 + 2 #2~14(A=14)

  def __repr__(self):
      return "{}".format(self._num)

class suit:

  def __init__(self, suit):
      red = "\033[91m"
      green = "\033[92m"
      yellow = "\033[93m"
      black = "\033[30m"
      white = "\033[37m"
      ENDC = "\033[0m"
      colors = [yellow,green,red,white]
      if mode:
        suits = ["♦︎", "♣︎", "❤︎", "♠︎"]
      else:
        suits = ["Diamond", "Club", "Heart", "Spade"]
      self._suit = suits[suit]
      self._color = colors[suit]

  def __repr__(self):
      return "{}".format(self._suit)

class card(num,suit):

  def __init__(self, Cnum, Csuit):
      self._num = num(Cnum)._num
      self._suit = suit(Csuit)._suit
      self._color = suit(Csuit)._color
      self._size = num(Cnum)._size
      self._show = True

  def __repr__(self):
      if self._show:
          if mode:
              return "\033[40m{}{} {}\033[0m".format(self._color, self._suit, self._num,)
          else:
              return "\033[40m{}{} of {}\033[0m".format(self._color,self._num, self._suit)
      else:
          return "\033[40m   \033[0m"


class deck(card):

  def __init__(self):
      self._deck = []
      for i in range(52):
          self._deck.append(card((i+1)%13,i//13))

  def __repr__(self):
      return "{}".format(self._deck)

  def shuffle(self):
      random.shuffle(self._deck)

class hand(card):

  def __init__(self, C1, C2, C3, C4, C5):

      numbers = [C1._size, C2._size, C3._size, C4._size, C5._size]
      numbers.sort()
      numbers.reverse()

      #フラッシュ判断
      if C1._suit == C2._suit == C3._suit == C4._suit == C5._suit:
          flush = True
      else:
          flush = False

      #ストレート判断
      if numbers[0] == 14 and numbers[1] == 5 and numbers[2] == 4 and numbers[3] == 3 and numbers [4] == 2:
          straight = True
      elif numbers[0] - numbers[1] == numbers[1] - numbers[2] == numbers[2] - numbers[3] == numbers[3] - numbers[4] == 1:
          straight = True
      else:
          straight = False

      #ペア判断
      if straight and flush:
          if numbers[4] == 10:
              self._hand = "Royal Flush"
              self._power = [10,14,13,12,11,10]
          else:
              self._hand = "Straight Flush"
              self._power = [9] + numbers
      elif flush:
          self._power = [6] + numbers
          self._hand = "Flush"
      elif straight:
          if numbers[0] == 14:
              self._power = [5,5,4,3,2,1]
              self._hand = "Straight"
          else:
              self._power = [5] + numbers
              self._hand = "Straight"
      elif numbers[0] == numbers[1] == numbers[2] == numbers[3] or numbers[1] == numbers[2] == numbers[3] == numbers[4]:
          self._hand = "Four of a Kind"
          if numbers[0] == numbers[3]:
              self._power = [8] + numbers
          else:
              self._power = [8] + numbers[1:] + numbers[0:1]
      elif numbers[0] == numbers[1] == numbers[2]:
          if numbers[3] == numbers[4]:
              self._hand = "Full House"
              self._power = [7] + numbers
          else:
              self._hand = "Three of a Kind"
              self._power = [4] + numbers
      elif numbers[1] == numbers[2] == numbers[3]:
          self._hand = "Three of a Kind"
          self._power = [4] + numbers[1:4] + numbers[0:1] + numbers[4:]
      elif numbers[2] == numbers[3] == numbers[4]:
          if numbers[0] == numbers[1]:
              self._hand = "Full House"
              self._power = [7] + numbers[2:] + numbers[:2]
          else:
              self._hand = "Three of a Kind"
              self._power = [4] + numbers[2:] + numbers[:2]
      elif numbers[0] > numbers[1] > numbers[2] > numbers[3] > numbers[4]:
          self._hand = "High Card"
          self._power = [1] + numbers
      elif (numbers[0] == numbers[1] and numbers[2] == numbers[3]):
          self._hand = "Two Pair"
          self._power = [3] + numbers
      elif (numbers[0] == numbers[1] and numbers[3] == numbers[4]):
          self._hand = "Two Pair"
          self._power = [3] + numbers[:2] + numbers[3:] + numbers[2:3]
      elif (numbers[1] == numbers[2] and numbers[3] == numbers[4]):
          self._hand = "Two Pair"
          self._power = [3] + numbers[1:] + numbers[:1]
      elif numbers[0] == numbers[1]:
          self._hand = "One Pair"
          self._power = [2] + numbers
      elif numbers[1] == numbers[2]:
          self._hand = "One Pair"
          self._power = [2] + numbers[1:3] + numbers[:1] + numbers[3:]
      elif numbers[2] == numbers[3]:
          self._hand = "One Pair"
          self._power = [2] + numbers[2:4] + numbers[:2] + numbers[4:]
      elif numbers[3] == numbers[4]:
          self._hand = "One Pair"
          self._power = [2] + numbers[3:] + numbers[:3]

      self._cards = [C1,C2,C3,C4,C5]

  def __repr__(self):
      return "{} ({})".format(self._hand, self._cards)

class pocketboard(hand):
  def __init__(self,seven):
      power = [0,0,0,0,0,0]
      for y in range(7):
          six = seven[:]
          del six[y]
          for z in range(y,6):
              five = six[:]
              del five[z]
              hands = hand(five[0], five[1], five[2], five[3], five[4])
              for n in range(6):
                  if hands._power[n] < power[n]:
                      break
                  elif hands._power[n] > power[n]:
                      judge = hands
                      power = hands._power
                      break
      self._cards = seven
      self._hand = judge
      self._power = power

  def __repr__(self):
      return "{}".format(self._hand)
