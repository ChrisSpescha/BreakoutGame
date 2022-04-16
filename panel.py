from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Panels(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.turtlesize(stretch_wid=1, stretch_len=3, outline=0)
        # self.setheading(180)
        self.goto(xcor, ycor)
