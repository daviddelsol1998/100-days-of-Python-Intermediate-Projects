from turtle import Turtle, Screen
import random

walker = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
walker.pensize(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def right():
    walker.fd(50)


def left():
    walker.bk(50)


def down():
    walker.rt(90)
    right()


def up():
    walker.lt(90)
    right()


direction = [right, left, up, down]

walker.speed('fastest')

for i in range(150):
    walker.pencolor(random_color())
    random.choice(direction)()

screen.exitonclick()
