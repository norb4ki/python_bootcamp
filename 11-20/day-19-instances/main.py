import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
contestants = []
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False
winner = ''

for step in range (6):
  racer = turtle.Turtle(shape="turtle")
  racer.penup()
  racer.color(colors[step])
  racer.goto(x = -230, y = -100 + step * 40)
  contestants.append(racer)

if user_bet:
  is_race_on = True

print(user_bet)
while is_race_on:
  for racer in contestants:
    distance = random.randint(0, 10)
    racer.forward(distance)
    position = racer.pos()
    print(position)
    if position[0] >= 230:
      is_race_on = False
      winner = racer.color()[0]
      break

if winner == user_bet:
  print(f'The winner is the {winner} turtle. You win!')
else:
  print(f'The winner is the {winner} turtle. You lose!')

screen.exitonclick()
