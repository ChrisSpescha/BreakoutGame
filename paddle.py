from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=10, outline=0)
        self.goto(x=xcor, y=ycor)

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
