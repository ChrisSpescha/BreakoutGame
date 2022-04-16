from turtle import Turtle


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 4
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.lives -=1
        self.goto(300, -300)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 30, "normal"))
