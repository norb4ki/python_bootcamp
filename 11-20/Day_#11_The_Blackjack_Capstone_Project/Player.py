class Player:
  def __init__(self):
    self.hand = []
    self.score = 0

  def deal_hand(self, deck):
    self.hand = [deck.pop(), deck.pop()]

  def take_card(self, deck):
    self.hand.append(deck.pop()) 

  def get_hand(self):
    return self.hand
  
  def get_score(self):
    return self.score
  
  def reset(self):
    self.hand = []
    self.score = 0
  
  def calculate_hand(self):
    acc = 0
    unreverted_ace = False

    for card in self.hand:
      if card == 11 and acc + card <= 21:
        unreverted_ace = True
        acc += 11
      elif card == 11:
        acc += 1
      elif acc + card > 21 and unreverted_ace:
        acc += card - 10
      else:
        acc += card
    self.score = acc

    return acc
