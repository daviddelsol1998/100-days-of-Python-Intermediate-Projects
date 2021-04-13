import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.bgcolor("black")


colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]


def draw_shape(num_sides):
    for i in range(num_sides):
        tim.forward(75)
        tim.right(360 / num_sides)


for i in range(3,10):
    tim.pencolor(random.choice(colors))
    draw_shape(i)

screen.exitonclick()
