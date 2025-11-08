from turtle import Turtle

DIRECTIONS = {
  "right": 0,
  "up": 90,
  "left": 180,
  "down": 270 
}
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake():
  def __init__(self):
    self.body = self.create_snake()
    self.turn_applied = True

  def create_snake(self):
    segments = []
    for position in STARTING_POSITIONS:
      segment = Turtle('square')
      segment.color('white')
      segment.penup()
      segment.goto(position)
      segments.append(segment)
    return segments

  def turn_right(self):
    # ignores backward turn attempt
    if self.body[0].heading() == DIRECTIONS["left"] or not self.turn_applied:
      return
    self.body[0].setheading(DIRECTIONS["right"])
    self.turn_applied = False

  def turn_left(self):
    # ignores backward turn attempt
    if self.body[0].heading() == DIRECTIONS["right"] or not self.turn_applied:
      return
    self.body[0].setheading(DIRECTIONS["left"])

  def turn_up(self):
    # ignores backward turn attempt
    if self.body[0].heading() == DIRECTIONS["down"] or not self.turn_applied:
      return
    self.body[0].setheading(DIRECTIONS["up"])    

  def turn_down(self):
    # ignores backward turn attempt
    if self.body[0].heading() == DIRECTIONS["up"]  or not self.turn_applied:
      return
    self.body[0].setheading(DIRECTIONS["down"])
  
  def move(self):
    for body_part in range(len(self.body) - 1, 0, -1):
      new_x = self.body[body_part - 1].xcor()
      new_y = self.body[body_part - 1].ycor()
      self.body[body_part].goto(new_x, new_y)
    self.body[0].forward(20)
    self.turn_applied = True