import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move_snake()

    # detect collision w food
    if snake.squares[0].distance(food) < 15:
        food.create_new()
        scoreboard.refresh_text()
        snake.add_square()

    # detect collision with wall
    if snake.squares[0].xcor() > 280 or snake.squares[0].xcor() < -280 or snake.squares[0].ycor() > 280 or \
            snake.squares[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for square in snake.squares[1:]:
        if snake.squares[0].distance(square) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
