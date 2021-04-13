import random
from turtle import Turtle, Screen

dot = Turtle()
screen = Screen()
screen.colormode(255)
dot.pensize(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_line():
    for _ in range(10):
        dot.penup()
        dot.dot(20, random_color())
        dot.fd(50)


y = -100
dot.hideturtle()
dot.speed('fastest')

for _ in range(10):
    dot.penup()
    dot.setposition(-300, y)
    draw_line()
    y += 40

screen.exitonclick()
