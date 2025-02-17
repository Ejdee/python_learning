from turtle import Turtle, Screen


def move_forward():
    tim.forward(5)


def move_backward():
    tim.back(5)


def turn_left():
    tim.left(5)


def turn_right():
    tim.right(5)


def clear_screen():
    tim.reset()


tim = Turtle()
screen = Screen()
screen.listen()

screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)

screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
