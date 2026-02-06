from turtle import Turtle

ALIGNMENT = 'center'
FONT_REGULAR = ('Arial', 16, 'normal')
FONT_BIG = ('Arial', 32, 'bold')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    with open("high_score.txt", 'r') as f:
      self.high_score = int(f.read())
    self.score = 0
    self.hideturtle()
    self.teleport(0, 260)
    self.color('white')
    self.write(f'Score: {self.score} High score: {self.high_score}', align=ALIGNMENT, font=FONT_REGULAR )

  def increase_score(self):
    self.clear()
    self.score += 1
    self.write(f'Score: {self.score} High score: {self.high_score}', align=ALIGNMENT, font=FONT_REGULAR )

  def game_over(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("high_score.txt", 'w') as f:
        f.write(f'{self.high_score}')
    self.clear()
    self.teleport(0, 40)
    self.write(f'GAME OVER', align=ALIGNMENT, font=FONT_BIG )
    self.teleport(0, 0)   
    self.write(f'Final score: {self.score}', align=ALIGNMENT, font=FONT_REGULAR )
  
  def reset(self):
    self.teleport(0, 260)
    self.score = 0
    self.clear()
    self.write(f'Score: {self.score} High score: {self.high_score}', align=ALIGNMENT, font=FONT_REGULAR )
