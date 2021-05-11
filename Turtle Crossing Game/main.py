import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

# create 10 cars at the beginning of the game
for _ in range(8):
    car_manager.create_car()

screen.listen()
screen.onkeypress(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in car_manager.car_list:
        car.move()
        if -281 > car.xcor() > -288:
            car.hideturtle()
            car_manager.car_list.remove(car)
            car_manager.create_car()
            print(car.move_distance)

    if player.ycor() == player.finish_line:
        score.update_score()
