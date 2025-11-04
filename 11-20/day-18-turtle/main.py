from turtle import Screen, Turtle, colormode
import random
import colorgram

tim = Turtle()
colormode(255)

def get_color_tuple():
  red = random.random()
  green = random.random()
  blue = random.random()

  return (red, green, blue)

def get_palette_from_image(path, num_of_colors):
  colors = colorgram.extract(path, num_of_colors)
  palette = []

  for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    palette.append((red, green, blue))
  
  return palette

def teleport_to_next_column(position, turtle):
  position["x"] += 50
  turtle.teleport(position["x"], position["y"])

def teleport_to_next_row(position, turtle):
  position["y"] += 50
  position["x"] = position[start_x]
  turtle.teleport(position["x"], position["y"])


palette = get_palette_from_image('./image.png', 100)
position = {
  "x": -225,
  "y": -225,
  "start_x": -225,
  "start_y": -225
}

tim.teleport(position["x"], position["y"])

for row in range(10):
  for column in range(10):
    color = random.choice(palette)
    tim.dot(20, color)
    teleport_to_next_column(position, tim)
  teleport_to_next_row(position, tim)

screen = Screen()
screen.exitonclick()