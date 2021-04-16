from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
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
score = Score()
print(f'score at the beginning {score.score_number}')

# todo set up snake control
screen.listen()
screen.onkeypress(fun=snake.up, key='Up')
screen.onkeypress(fun=snake.down, key='Down')
screen.onkeypress(fun=snake.left, key='Left')
screen.onkeypress(fun=snake.right, key='Right')

game_is_on = True

# temporal code to set score to zero
score.score_number -= 1

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()

        score.score_point()

        # to be added later snake.add_snake_part()

    snake.move()

screen.exitonclick()
