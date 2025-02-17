from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user = screen.textinput(title="Welcome to turtle race!", prompt="Who do you think is gonna win?")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y = -90

all_tims = []

for i in range(len(colors)):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230, y=y)
    y += 30
    tim.color(colors[i])
    all_tims.append(tim)

if user:
    is_race_on = True

while is_race_on:

    for tim in all_tims:
        r_number = randint(0, 10)
        tim.forward(r_number)
        if tim.xcor() > 220:
            is_race_on = False
            color_of_tim = tim.pencolor()
            if user == color_of_tim:
                print(f"You won. The {color_of_tim} turtle has won!")
            else:
                print(f"You lose. The {color_of_tim} turtle has won!")


screen.exitonclick()
