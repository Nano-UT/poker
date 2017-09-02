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
      self._size = (num + 11) % 13 + 2

  def __repr__(self):
      return "{}".format(self._num)

class suit:

  def __init__(self, suit):
      if mode:
        suits = ["♦︎", "♣︎", "❤︎", "♠︎"]
      else:
        suits = ["Diamond", "Club", "Heart", "Spade"]
      self._suit = suits[suit]

  def __repr__(self):
      return "{}".format(self._suit)

class card(num,suit):

  def __init__(self, Cnum, Csuit):
      self._num = num(Cnum)._num
      self._suit = suit(Csuit)._suit
      self._size = num(Cnum)._size

  def __repr__(self):
      if mode:
        return "{} {}".format(self._suit, self._num)
      else:
        return "{} of {}".format(self._num, self._suit)

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

      #フラッシュ判断
      if C1._suit == C2._suit == C3._suit == C4._suit == C5._suit:
          flush = True
      else:
          flush = False

      numbers = [C1._size, C2._size, C3._size, C4._size, C5._size]
      numbers.sort()

      Chand = 0

      #ストレート判断
      if numbers[0] == 0 and numbers[1] == 1 and numbers[2] == 2 and numbers[3] == 3 and numbers [4] == 12:
          straight = True
      elif numbers[0] >= 1 and numbers[4] - numbers[3] == numbers[3] - numbers[2] == numbers[2] - numbers[1] == numbers[1] - numbers[0] == 1:
          straight = True
      else:
          straight = False

      #ペア判断
      if numbers[0] == numbers[1] == numbers[2] == numbers[3] or numbers[1] == numbers[2] == numbers[3] == numbers[4]:
          Chand = 4
      elif numbers[0] == numbers[1] == numbers[2]:
          if numbers[3] == numbers[4]:
              Chand = 5
          else:
              Chand = 3
      elif numbers[1] == numbers[2] == numbers[3]:
          Chand = 3
      elif numbers[2] == numbers[3] == numbers[4]:
          if numbers[0] == numbers[1]:
              Chand = 5
          else:
              Chand = 3
      elif numbers[0] < numbers[1] < numbers[2] < numbers[3] < numbers[4]:
          Chand = 0
      elif (numbers[0] == numbers[1] and numbers[2] == numbers[3]) or (numbers[0] == numbers[1] and numbers[3] == numbers[4]) or (numbers[1] == numbers[2] and numbers[3] == numbers[4]):
          Chand = 2
      else:
          Chand = 1

      self._num = []
      self._cards = [C1,C2,C3,C4,C5]

      for i in range(5):
          self._num.append(numbers[4-i])

      if straight and flush:
          self._hand = "Straight Flush"
          self._power = 9
      elif Chand == 4:
          self._hand = "Four of a Kind"
          self._power = 8
      elif Chand == 5:
          self._hand = "Full House"
          self._power = 7
      elif flush:
          self._hand = "Flush"
          self._power = 6
      elif straight:
          self._hand = "Straight"
          self._power = 5
      elif Chand == 3:
          self._hand = "Three of a Kind"
          self._power = 4
      elif Chand == 2:
          self._hand = "Two Pair"
          self._power = 3
      elif Chand == 1:
          self._hand = "One Pair"
          self._power = 2
      elif Chand == 0:
          self._hand = "High Card"
          self._power = 1
      else:
          self._hand = "Error!!!"
          self._power = False

  def __repr__(self):
      return "{} ({})".format(self._hand, self._cards)

class pocketboard(hand):
  def __init__(self,seven):
      power = 0
      for y in range(7):
          six = seven[:]
          del six[y]
          for z in range(y,6):
              five = six[:]
              del five[z]
              hands = hand(five[0], five[1], five[2], five[3], five[4])
              if hands._power > power:
                  power = hands._power
                  judge = hands
              elif hands._power == power:
                  for n in range(5):
                      if hands._num[n] > judge._num[n]:
                          judge = hands
                          break
      self._hand = judge
      self._power = [judge._power] + judge._num
      #課題は、役 ラグの順にpowerを決めることと、A~5ストレートの扱い

  def __repr__(self):
      return "{}".format(self._hand)
