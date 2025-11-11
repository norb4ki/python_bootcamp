from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("red")

    self.refresh()

  def refresh(self):
    random_x = random.randint(-280, 299)
    random_x -= random_x % 20
    random_y = random.randint(-280, 299)
    random_y -= random_y % 20
    self.teleport(random_x, random_y)