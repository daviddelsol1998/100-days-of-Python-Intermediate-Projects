from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def create_car(self):
        possibility = random.randint(1, 6)

        if possibility == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.move_distance)
