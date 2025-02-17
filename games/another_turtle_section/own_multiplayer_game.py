from turtle import Turtle, Screen


def draw_lines():
    lines.penup()
    lines.goto(x=-220, y=-200)
    lines.pendown()
    lines.setheading(90)
    lines.goto(x=-220, y=200)
    lines.penup()
    lines.goto(x=230, y=200)
    lines.pendown()
    lines.goto(x=230, y=-200)
    lines.hideturtle()


def move_tim():
    tim.forward(10)


def move_tom():
    tom.forward(10)


screen = Screen()
screen.setup(width=500, height=400)

user = screen.textinput(title="Welcome to turtle race!", prompt="Type (start) to begin.")

tim = Turtle(shape='turtle')
tom = Turtle(shape='turtle')

lines = Turtle()
draw_lines()

tim.color('red')
tom.color('blue')

tim.penup()
tom.penup()

tim.goto(x=-230, y=-50)
tom.goto(x=-230, y=50)

screen.listen()

screen.onkey(fun=move_tom, key='a')
screen.onkey(fun=move_tim, key='l')

screen.exitonclick()
