import random
from turtle import Turtle, Screen

tim = Turtle()

geometric_shapes = {
    'triangle': 3,
    'rectangle': 4,
    'pentagon': 5,
    'hexagon': 6,
    'heptagon': 7,
    'octagon': 8,
    'nonagon': 9,
    'decagon': 10
}

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]


def draw_shape(num_sides):
    for i in range(num_sides):
        tim.forward(75)
        tim.right(360 / num_sides)


for shape in geometric_shapes:
    tim.pencolor(random.choice(colors))
    draw_shape(geometric_shapes[shape])

screen = Screen()
screen.exitonclick()
