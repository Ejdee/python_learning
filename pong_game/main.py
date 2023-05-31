import time
from turtle import Screen, Turtle
from mid_line import Midline
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1100, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

half_line = Midline()
r_paddle = Paddle(500, 0)
l_paddle = Paddle(-500, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='Down', fun=r_paddle.down)
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeypress(key='s', fun=l_paddle.down)

game_on = True
collision_up = 0
collision_down = 0

while game_on:
    screen.update()
    time.sleep(0.025)
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 480 or ball.distance(l_paddle) < 50 and ball.xcor() < -480:
        ball.bounce_x()

    # detect misses
    if ball.xcor() > 550:
        ball.reset()
        scoreboard.update_left()

    if ball.xcor() < -550:
        ball.reset()
        scoreboard.update_right()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
