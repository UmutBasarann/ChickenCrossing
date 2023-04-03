from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

is_game_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

while is_game_on:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()

    if player.ycor() > 290:
        scoreboard.level_up()
        player.reset_position()
        player.increase_move_distance()
        car_manager.increase_move_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
