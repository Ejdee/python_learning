from turtle import Turtle
PLAYER_MOVEMENT = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(x=0, y=-280)
        self.color('white')
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + PLAYER_MOVEMENT
        self.goto(x=self.xcor(), y=new_y)

    def reset(self):
        self.goto(x=0, y=-280)