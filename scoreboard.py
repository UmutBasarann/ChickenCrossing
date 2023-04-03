from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")
SPAWN_POSITION = (-250, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(SPAWN_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.hideturtle()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
