from turtle import Screen
from paddle import Paddle
from ball import Ball
from levels import Level
from scoreboard import Scoreboard
from lives import Lives
import time
LEVEL = 1
pad = Paddle(0, -250)
ball = Ball()
level = Level()
scoreboard = Scoreboard()
lives = Lives()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Break Out")
screen.tracer(0)

screen.listen()
screen.onkey(pad.move_left, "a")
screen.onkey(pad.move_right, "d")


game_is_on = True
level.load_panels(LEVEL)
while game_is_on:

    screen.update()
    time.sleep(0.01)
    ball.move()

    if not level.panel_list:
        scoreboard.new_level()
        ball.new_ball()
        LEVEL += 1
        level.load_panels(LEVEL)

    # Detect Collision with panel
    for panel in level.panel_list:
        if ball.distance(panel) < 40:
            ball.bounce_y()
            level.panel_list.remove(panel)
            panel.hideturtle()

    # Detect collision with ceiling
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect Collision with walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect Collision with paddle
    if ball.distance(pad) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Detect paddle miss
    if ball.ycor() < -280:
        ball.new_ball()
        lives.update_lives()
        if lives.lives < 1:
            scoreboard.you_lose()
            game_is_on = False

screen.exitonclick()
