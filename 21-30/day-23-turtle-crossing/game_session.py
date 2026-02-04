from turtle import Screen, ontimer
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random


LEVELS = {
    1: {'car_move_period': 500, 'car_count': 20, "generate_car_probability": 0.15},
    2: {'car_move_period': 400, 'car_count': 25, "generate_car_probability": 0.2},
    3: {'car_move_period': 300, 'car_count': 35, "generate_car_probability": 0.25},
    4: {'car_move_period': 200, 'car_count': 40, "generate_car_probability": 0.3},
    5: {'car_move_period': 100, 'car_count': 45, "generate_car_probability": 0.5},
}
class GameSession:
  def __init__(self):
    self.screen = Screen()
    self.screen.setup(width=600, height=600)
    self.screen.tracer(0)
    self.player = Player()
    self.car_manager = CarManager()
    self.scoreboard = Scoreboard()

    self.screen.onkeypress(fun=self.player.move, key='w')
    self.screen.listen()

    self.is_game_on = True
    self.level = 1
    self.start()

  def is_collision(self):
    for car in self.car_manager.cars:
      x_diff = abs(car.xcor() - self.player.xcor())
      y_diff = abs(car.ycor() - self.player.ycor())
      if x_diff < 40 and y_diff < 20:
        return True
    return False
  
  def start(self):
    while self.is_game_on:
      if self.is_collision():
        self.scoreboard.game_over()
        self.is_game_on = False
      if self.player.ycor() > 280:
        self.level_up()
      self.car_manager.move_cars()
      if random.random() < LEVELS[self.level]["generate_car_probability"]:
        self.car_manager.generate_car()
      time.sleep(0.1)
      self.screen.update()
    self.screen.exitonclick()


  def reset(self):
    self.player.reset_position()
    self.car_manager.delete_all_cars()
    self.car_manager.setup_cars(LEVELS[self.level]["car_count"])

  def level_up(self):
    self.level += 1
    self.scoreboard.increase_level()
    self.reset()


  