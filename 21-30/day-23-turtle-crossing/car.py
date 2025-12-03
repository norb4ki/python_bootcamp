from turtle import Turtle

class Car(Turtle):
  def __init__(self, position, color, border):
    super().__init__()
    self.teleport(position[0], position[1])
    self.shape('square')
    self.color(color)
    self.shapesize(1, 3)
    print('in car')