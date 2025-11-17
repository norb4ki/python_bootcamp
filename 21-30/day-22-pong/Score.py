from turtle import Turtle

class Score:
  def __init__(self):
    self.r_score = 0
    self.l_score = 0

    self.start_message = Turtle()
    self.start_message.penup()
    self.start_message.color('white')
    self.start_message.hideturtle()
    self.start_message.teleport(0, 50)
    self.show_start_message()

    # setup score message
    self.score_message = Turtle()
    self.score_message.penup()
    self.score_message.color('white')
    self.score_message.hideturtle()
    self.score_message.teleport(0, 250)
    self.score_message.write(arg=f'{self.l_score}:{self.r_score}', align='center', font=('Arial', '32', 'bold'))

  def update_score(self):
    self.score_message.clear()
    self.score_message.write(arg=f'{self.l_score}:{self.r_score}', align='center', font=('Arial', '32', 'bold'))

  def show_start_message(self):
    self.start_message.write(arg='PRESS SPACE TO START A GAME\n\nPRESS "W" AND "S" TO CONTROL LEFT PADDLE\nPRESS ARROW_UP AND ARROW_DOWN TO CONTROL RIGHT PADDLE', align='center', font=('Arial', 16, 'normal'))

  def hide_start_message(self):
    self.start_message.clear()