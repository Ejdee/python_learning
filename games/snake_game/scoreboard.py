from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        self.write_text()

    def write_text(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest score: {self.high_score}", move=True, align='center', font=FONT)

    def refresh_text(self):
        self.goto(x=0, y=270)
        self.clear()
        self.score += 1
        self.write_text()

    def reset(self):
        self.goto(x=0, y=270)
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.write_text()
