from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, user_x, user_y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(x=user_x, y=user_y)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
