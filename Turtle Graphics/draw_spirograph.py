from turtle import Turtle, Screen
import random

circle = Turtle()
screen = Screen()
screen.colormode(255)
circle.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


angle = 0

for _ in range(100):
    circle.pencolor(random_color())
    circle.circle(100)
    angle += 1
    circle.rt(angle)

screen.exitonclick()
