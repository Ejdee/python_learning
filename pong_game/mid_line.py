from turtle import Turtle


class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.pensize(10)
        self.color("white")
        self.penup()
        self.goto(x=0, y=-300)
        self.setheading(90)
        self.draw_line()
        self.hideturtle()

    def draw_line(self):
        for i in range(16):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(30)
