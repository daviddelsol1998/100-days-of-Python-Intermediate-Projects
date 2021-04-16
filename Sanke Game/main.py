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

# todo set up snake control
screen.listen()
screen.onkeypress(fun=snake.up,key='Up')
screen.onkeypress(fun=snake.down,key='Down')
screen.onkeypress(fun=snake.left,key='Left')
screen.onkeypress(fun=snake.right,key='Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
