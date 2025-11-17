from turtle import Turtle
from utils import BALL_HEADINGS
import random

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('white')
    self.setheading(random.choice(BALL_HEADINGS))
    self.speed('fastest')
    

  def bounce_x(self):
    current_heading = self.heading()
    if current_heading > 180:
      new_heading = 540 - current_heading
    else:
      new_heading = 180 - current_heading
    
    self.setheading(new_heading)

  def bounce_y(self):
    current_heading = self.heading()
    new_heading = 360 - current_heading
    self.setheading(new_heading)

  def move(self):
    self.forward(10)

  def reset(self):
    self.setheading(random.choice(BALL_HEADINGS))
    self.teleport(0, 0)

  

      

