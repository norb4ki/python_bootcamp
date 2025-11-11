from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

BORDER_RIGHT = 280
BORDER_LEFT = -280
BORDER_UP = 280
BORDER_DOWN = -280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake')
screen.tracer(0)
snake = Snake()
screen.onkey(snake.turn_down, 'Down')
screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_right, 'Right')
screen.onkey(snake.turn_left, 'Left')
screen.listen()
food = Food()
score = Scoreboard()

def game_loop():
  game_is_over = False

  snake.move()
  screen.update()

  # Detect collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.grow()
    score.increase_score()

  head_pos_x = snake.head.xcor()
  head_pos_y = snake.head.ycor()

  # Detect collision with the wall
  if head_pos_x > BORDER_RIGHT or head_pos_x < BORDER_LEFT or head_pos_y > BORDER_UP or head_pos_y < BORDER_DOWN:
    score.game_over()
    game_is_over = True
  
  # Detect collision with the tail
  for index in range(1, snake.len):
    if snake.head.distance(snake.body[index]) < 15:
      score.game_over()
      game_is_over = True
  
  if not game_is_over:
    screen.ontimer(game_loop, 100)


game_loop()  # start the loop
screen.mainloop()