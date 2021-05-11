from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE * random.uniform(0.8, 1.6)
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(270, random.randint(-250, 260))

    def move(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.move_distance *= MOVE_INCREMENT


class CarManager:
    def __init__(self):
        self.car_list = []

    def create_car(self):
        self.car_list.append(Car())
