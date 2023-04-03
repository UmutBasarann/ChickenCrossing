from turtle import Turtle
import random

SHAPE = "square"
COLORS = ["blue", "yellow", "purple", "red", "green", "orange", "cyan", "white", "gray"]
MOVE_DISTANCE = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_speed = 0.1

    def spawn_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_car = Turtle(SHAPE)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=0.5, stretch_len=0.8)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 280))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)

    def increase_move_speed(self):
        self.move_speed *= 0.4
