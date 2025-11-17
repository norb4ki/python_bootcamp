from turtle import Turtle

class Score:
  def __init__(self):
    self.r_score = 0
    self.l_score = 0

    # setup score message
    self.score_message = Turtle()
    self.score_message.penup()
    self.score_message.color('white')
    self.score_message.hideturtle()
    self.score_message.teleport(0, 250)
    self.score_message.write(arg=f'{self.l_score}:{self.r_score}', align='center', font=('Arial', '32', 'bold'))

  def update(self):
    self.score_message.clear()
    self.score_message.write(arg=f'{self.l_score}:{self.r_score}', align='center', font=('Arial', '32', 'bold'))
