from turtle import Turtle

directions = {
  "right": 0,
  "down": 90,
  "left": 180,
  "up": 270 
}

class Snake():
  def __init__(self):
    self.heading = directions["right"]
    self.body = []
    self.head_position = 

  def turn_right(self):
    # ignores backward turn attempt
    if self.heading == directions["left"]:
      return
    self.heading = directions["right"]

  def turn_left(self):
    # ignores backward turn attempt
    if self.heading == directions["up"]:
      return
    self.heading = directions["down"]

  def turn_up(self):
    # ignores backward turn attempt
    if self.heading == directions["right"]:
      return
    self.heading = directions["left"]

  def turn_down(self):
    # ignores backward turn attempt
    if self.heading == directions["down"]:
      return
    self.heading = directions["up"]
  