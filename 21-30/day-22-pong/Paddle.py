from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, pos_x, pos_y = 0):
    super().__init__()
    self.penup()
    self.teleport(pos_x, pos_y)
    self.color('white')
    self.shape('square')
    self.shapesize(1, 5)
    self.speed('fastest')
    self.left(90)

  def move_up(self):
    if self.ycor() < 250:
      self.forward(20)
  
  def move_down(self):
    if self.ycor() > -250:
      self.backward(20)