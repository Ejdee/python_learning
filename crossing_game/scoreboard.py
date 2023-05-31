from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.write_text()

    def write_text(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.write(arg=f"Level: {self.level}", align='left', font=("Courier", 20, 'normal'))

    def game_over(self):
        self.color('white')
        self.hideturtle()
        self.goto(0, 0)
        self.penup()
        self.write(arg="GAME OVER", align='center', font=("Courier", 80, 'normal'))

    def update(self):
        self.clear()
        self.level += 1
        self.write_text()
