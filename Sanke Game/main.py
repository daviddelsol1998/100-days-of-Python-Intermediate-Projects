from turtle import Screen
from snake import Snake
import time

# todo setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game by David Del Sol using Python Turtle')
screen.tracer(0)

# todo setup snake
snake = Snake()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
