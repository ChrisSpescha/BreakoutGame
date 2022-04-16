from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-300, -300)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 30, "normal"))

    def new_level(self):
        self.level += 1
        self.update_level()

    def you_lose(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU LOSE", align="center", font=("Courier", 30, "normal"))

