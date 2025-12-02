from turtle import Screen
from player import Player

class GameSession:
  def __init__(self):
    self.screen = Screen()
    self.screen.setup(width=600, height=600)

    self.player = Player()
    self.player.reset_position()

    self.screen.onkeypress(fun=self.player.move, key='w')
    self.screen.listen()
    