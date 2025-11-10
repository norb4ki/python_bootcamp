from turtle import Turtle

ALIGNMENT = 'center'
FONT_REGULAR = ('Arial', 16, 'normal')
FONT_BIG = ('Arial', 32, 'bold')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.score = 0
    self.hideturtle()
    self.teleport(0, 260)
    self.color('white')
    self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT_REGULAR )

  def increase_score(self):
    self.clear()
    self.score += 1
    self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT_REGULAR )

  def game_over(self):
    self.clear()
    self.teleport(0, 40)
    self.write(f'GAME OVER', align=ALIGNMENT, font=FONT_BIG )
    self.teleport(0, 0)   
    self.write(f'Final score: {self.score}', align=ALIGNMENT, font=FONT_REGULAR )
