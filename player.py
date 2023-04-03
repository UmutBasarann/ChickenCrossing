from turtle import Turtle

SHAPE = "turtle"
COLOR = "white"
SPAWN_POSITION = (0, -280)
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.move_distance = 20
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(SPAWN_POSITION)
        self.setheading(UP)

    def move(self):
        up_y = self.ycor() + self.move_distance
        self.goto(self.xcor(), up_y)

    def reset_position(self):
        self.goto(SPAWN_POSITION)

    def increase_move_distance(self):
        self.move_distance += 5
