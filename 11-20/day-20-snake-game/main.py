from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

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
  snake.move()
  screen.update()
  screen.ontimer(game_loop, 100)  # move every 100 ms (~10 FPS)

  # Detect collision with food
  if snake.head.distance(food) < 15:
    print('eat it')
    food.refresh()
    snake.grow()
    score.increase_score()

game_loop()  # start the loop
screen.mainloop()