import turtle
from Paddle import Paddle
class GameSession:
  def __init__ (self):
    self.is_on = True
    self.screen = turtle.Screen()
    self.screen.setup(800, 600)
    self.screen.bgcolor('black')
    self.screen.title('Pong')
    self.r_paddle = Paddle(350)
    self.l_paddle = Paddle(-350)

    self.screen.listen()
    self.screen.onkey(key='Up', fun=self.r_paddle.move_up)
    self.screen.onkey(key='Down', fun=self.r_paddle.move_down)

    self.screen.onkey(key='w', fun=self.l_paddle.move_up)
    self.screen.onkey(key='s', fun=self.l_paddle.move_down)

