import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
radius = 100
tim.speed(100)
heading = 3


def draw_circle(head):
    tim.circle(radius)
    tim.setheading(head)


for i in range(120):
    if i % 2 == 0:
        tim.color("red")
    else:
        tim.color("black")
    draw_circle(heading)
    heading += 3

t.exitonclick()