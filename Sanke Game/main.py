from turtle import Screen
from snake import Snake
from food import Food
import time

# todo setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game by David Del Sol using Python Turtle')
screen.tracer(0)

# todo setup snake
snake = Snake()
food = Food()

# todo set up snake control
screen.listen()
screen.onkeypress(fun=snake.up, key='Up')
screen.onkeypress(fun=snake.down, key='Down')
screen.onkeypress(fun=snake.left, key='Left')
screen.onkeypress(fun=snake.right, key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # todo detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_snake_part()


    snake.move()

screen.exitonclick()
