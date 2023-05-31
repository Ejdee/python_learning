import turtle as t
import random

tim = t.Turtle()

degrees = 360
base_distance = 100
n_of_sides = 3
t.colormode(255)
tim.pensize(50)
tim.speed(50)


def draw_shape(sides, distance):
    angle = degrees/sides
    tim.color(random.randint(0, 255),
              random.randint(0, 255),
              random.randint(0, 255)
              )
    for i in range(sides):
        tim.forward(distance)
        tim.right(angle)


for i in range(9):
    draw_shape(n_of_sides, base_distance)
    n_of_sides += 1


screen = t.Screen()
screen.exitonclick()
