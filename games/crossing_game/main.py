import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.move, key='Up')

game_on = True
i = 0

while game_on:
    screen.update()
    time.sleep(0.1)

    new_car = cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if player.distance(car) < 30:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reset()
        cars.faster()
        scoreboard.update()

screen.exitonclick()




