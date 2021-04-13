from turtle import Turtle, Screen
import random

walker = Turtle()
screen = Screen()
screen.bgcolor("black")
walker.pensize(10)

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]


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
    walker.pencolor(random.choice(colors))
    random.choice(direction)()

screen.exitonclick()
