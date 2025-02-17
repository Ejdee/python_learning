from turtle import Turtle

MOVE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.squares = []
        self.first = 0
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            square = Turtle(shape='square')
            square.color('white')
            square.penup()
            square.goto(x=self.first, y=0)
            self.first -= 20
            self.squares.append(square)

    def move_snake(self):
        for i in range(len(self.squares) - 1, 0, -1):
            self.squares[i].goto(self.squares[i - 1].xcor(), self.squares[i - 1].ycor())
        self.squares[0].forward(MOVE)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def add_square(self):
        square = Turtle(shape='square')
        square.color('white')
        square.penup()
        square.goto(x=self.squares[-1].xcor(), y=self.squares[-1].ycor())
        self.squares.append(square)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.first = 0
