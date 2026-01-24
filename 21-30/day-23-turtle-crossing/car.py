from turtle import Turtle

class Car(Turtle):
  def __init__(self, position, color, border):
    super().__init__()
    self.start_position = [border, position[1]]
    self.teleport(position[0], position[1])
    self.shape('square')
    self.color(color)
    self.shapesize(1, 3)
    self.penup()

  def move(self, distance):
    self.backward(distance)

  def crossed_border(self, border):
    return self.xcor() < border