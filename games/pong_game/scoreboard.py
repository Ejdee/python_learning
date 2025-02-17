from turtle import Turtle

FONT = ("Courier", 70, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.write_text()

    def write_text(self):
        self.goto(x=-100, y=200)
        self.write(arg=self.l_score, align='center', font=FONT)
        self.goto(x=100, y=200)
        self.write(arg=self.r_score, align='center', font=FONT)

    def update_left(self):
        self.l_score += 1
        self.clear()
        self.write_text()

    def update_right(self):
        self.r_score += 1
        self.clear()
        self.write_text()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=FONT)
