from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
from utils import COLOR_BG, BORDER_DOWN, BORDER_LEFT, BORDER_RIGHT, BORDER_UP, SCREEN_WIDTH, SCREEN_HEIGHT 

class GameSession:
  def __init__(self):
    self.screen = Screen()
    self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    self.screen.bgcolor(COLOR_BG)
    self.screen.title('Snake')
    self.screen.tracer(0)
    self.snake = Snake()
    self.screen.onkey(self.snake.turn_down, 'Down')
    self.screen.onkey(self.snake.turn_up, 'Up')
    self.screen.onkey(self.snake.turn_right, 'Right')
    self.screen.onkey(self.snake.turn_left, 'Left')
    self.screen.listen()
    self.food = Food()
    self.score = Scoreboard()
    self.game_is_over = False

  def start(self):
    self.snake.move()
    self.screen.update()

    # Detect collision with food
    if self.snake.head.distance(self.food) < 15:
      self.food.refresh()
      self.snake.grow()
      self.score.increase_score()

    head_pos_x = self.snake.head.xcor()
    head_pos_y = self.snake.head.ycor()

    # Detect collision with the wall
    if head_pos_x > BORDER_RIGHT or head_pos_x < BORDER_LEFT or head_pos_y > BORDER_UP or head_pos_y < BORDER_DOWN:
      self.game_over()
    
    # Detect collision with the tail
    for segment in self.snake.body[1:]:
      if self.snake.head.distance(segment) < 15:
        self.game_over()
    
    if not self.game_is_over:
      self.screen.ontimer(self.start, 100)

  def game_over(self):
    self.score.game_over()
    self.game_is_over = True
    self.screen.onkey(self.reset, 'space')

  def reset(self):
    self.snake.reset()
    self.score.reset()
    self.game_is_over = False
    self.start()