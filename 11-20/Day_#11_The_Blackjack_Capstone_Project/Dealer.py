from Player import Player

class Dealer(Player):
  visible_hand = []
  def __init__(self):
    super().__init__()

  def deal_hand(self, deck):
    super().deal_hand(deck)
    self.visible_hand.append(self.hand[0])
    self.calculate_hand()

  def get_hand(self):
    return self.visible_hand

  def turn(self, deck):
    while(self.score < 17):
      self.take_card(deck)
      self.calculate_hand()
    self.visible_hand = self.hand

  def reset(self):
    super().reset()
    self.visible_hand = []
  