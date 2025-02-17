import random
from turtle import Turtle
INCREMENT = 5
COLORS = ['red', 'blue', 'green', 'white', 'orange', 'purple', 'cyan']


class Cars:
    def __init__(self):
        self.all_cars = []
        self.starting_move = 5

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_y = random.randint(-230, 230)
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=new_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.starting_move)

    def faster(self):
        self.starting_move += INCREMENT