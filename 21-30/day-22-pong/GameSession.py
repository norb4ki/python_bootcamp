import turtle
from Paddle import Paddle
from Ball import Ball
class GameSession:
  def __init__ (self):
    self.is_on = True
    self.screen = turtle.Screen()
    self.screen.setup(800, 600)
    self.screen.bgcolor('black')
    self.screen.title('Pong')
    self.r_paddle = Paddle(350)
    self.l_paddle = Paddle(-350)
    self.ball = Ball()

    self.screen.listen()
    self.screen.onkey(key='Up', fun=self.r_paddle.move_up)
    self.screen.onkey(key='Down', fun=self.r_paddle.move_down)

    self.screen.onkey(key='w', fun=self.l_paddle.move_up)
    self.screen.onkey(key='s', fun=self.l_paddle.move_down)

  def start(self):
    self.ball.move()
    self.bounce_check()

    self.screen.ontimer(self.start, 20)

  def bounce_check(self):
    ball_x = self.ball.xcor()
    ball_y = self.ball.ycor()

    # Wall bounce
    if ball_y > 290 or ball_y < -290:
      self.ball.bounce_y()

    # Paddle bounce
    if(
      self.paddle_bounce_check(self.l_paddle, ball_x, ball_y)
      or self.paddle_bounce_check(self.r_paddle, ball_x, ball_y)
    ):
      
      self.ball.bounce_x()

  def paddle_bounce_check(self, paddle, ball_x, ball_y):
    paddle_x = paddle.xcor()
    paddle_y = paddle.ycor()
    return (
      paddle_x - 10 <= ball_x <= paddle_x + 5
      and paddle_y - 50 <= ball_y <= paddle_y + 50
    )