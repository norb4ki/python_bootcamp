from turtle import Screen
from player import Player
from car_manager import CarManager
class GameSession:
  def __init__(self):
    self.screen = Screen()
    self.screen.setup(width=600, height=600)

    self.player = Player()
    self.car_manager = CarManager()

    self.screen.onkeypress(fun=self.player.move, key='w')
    self.screen.listen()
    # self.screen.exitonclick()

  