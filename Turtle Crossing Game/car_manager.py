from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(270, random.randint(-270, 270))

    def move(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
