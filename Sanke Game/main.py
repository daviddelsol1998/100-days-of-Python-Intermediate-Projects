from turtle import Turtle, Screen
import time

# todo setup screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game by David Del Sol using Python Turtle')
screen.tracer(0)

# todo setup snake
snake_parts = []
x = 0

for i in range(3):
    new_snake_part = Turtle('square')
    new_snake_part.color('white')
    new_snake_part.penup()
    new_snake_part.setx(x)
    x -= 20
    snake_parts.append(new_snake_part)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    for snake_part in snake_parts:
        snake_part.fd(20)


screen.exitonclick()