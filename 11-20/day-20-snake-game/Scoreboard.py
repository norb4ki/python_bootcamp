from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.score = 0
    self.hideturtle()
    self.teleport(0, 260)
    self.color('white')
    self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal') )

  def increase_score(self):
    self.clear()
    self.score += 1
    self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal') )
