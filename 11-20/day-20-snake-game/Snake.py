from turtle import Turtle

DIRECTIONS = {
  "right": 0,
  "up": 90,
  "left": 180,
  "down": 270 
}
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
STEP = 20

class Snake():
  def __init__(self):
    self.len = 0
    self.body = self.create_snake()
    self.head = self.body[0]
    self.turn_applied = True

  def create_snake(self):
    segments = []
    for position in STARTING_POSITIONS:
      segment = self.add_piece(position, 'white')
      segments.append(segment)
    return segments

  def turn_right(self):
    # ignores backward turn attempt
    if self.head.heading() != DIRECTIONS["left"] and self.turn_applied:
      self.head.setheading(DIRECTIONS["right"])
      self.turn_applied = False

  def turn_left(self):
    # ignores backward turn attempt
    if self.head.heading() != DIRECTIONS["right"] and self.turn_applied:
      self.head.setheading(DIRECTIONS["left"])
      self.turn_applied = False


  def turn_up(self):
    # ignores backward turn attempt
    if self.head.heading() != DIRECTIONS["down"] and self.turn_applied:
      self.head.setheading(DIRECTIONS["up"])  
      self.turn_applied = False


  def turn_down(self):
    # ignores backward turn attempt
    if self.head.heading() != DIRECTIONS["up"]  and self.turn_applied:
      self.head.setheading(DIRECTIONS["down"])
      self.turn_applied = False

  def add_piece(self, position, color):
    segment = Turtle('square')
    segment.color(color)
    segment.penup()
    segment.goto(position)
    self.len += 1
    return segment

  def grow(self):
    tail_position_x = self.body[-1].xcor()
    tail_position_y = self.body[-1].ycor()
  
    segment = self.add_piece((tail_position_x, tail_position_y), 'green')
    self.body.append(segment)
  
  def move(self):
    for body_part in range(len(self.body) - 1, 0, -1):
      new_x = self.body[body_part - 1].xcor()
      new_y = self.body[body_part - 1].ycor()
      self.body[body_part].goto(new_x, new_y)
    self.head.forward(STEP)
    self.turn_applied = True