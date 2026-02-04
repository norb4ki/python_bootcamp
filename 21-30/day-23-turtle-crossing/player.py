from turtle import Turtle

STARTING_POSITION = [0, -280]
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, shape='turtle'):
        super().__init__(shape)
        self.left(90)
        self.penup()
        self.reset_position()
        
    def reset_position(self):
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])


    def move(self):
        self.forward(MOVE_DISTANCE)