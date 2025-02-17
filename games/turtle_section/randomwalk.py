import turtle as t
import random

tim = t.Turtle()

tim.pensize(15)
tim.speed(15)

t.colormode(255)

degrees = [90, 180, 270, 360]

while True:
    tim.color(random.randint(0, 255),
              random.randint(0, 255),
              random.randint(0, 255)
              )
    tim.forward(20)
    tim.right(random.choice(degrees))
