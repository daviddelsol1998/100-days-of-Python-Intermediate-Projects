from os import read
from turtle import Turtle, mode

TOP = (0, 270)
CENTER = (0,0)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(TOP)
        self.draw_score()

    def read_high_score(self):
        with open('high_score.txt', mode='r') as high_score_file:
            high_score = high_score_file.read()
            return int(high_score)

    def write_high_score(self):
        new_score = self.score_number
        with open('high_score.txt', mode='w') as high_score_file:
            high_score_file.write(str(new_score))

    def draw_score(self):
        self.clear()
        self.write(f'Score:{self.score_number} - High Score:{self.high_score}', align='center', font=("Arial", 20, "normal"))

    # def game_over(self):
    #     self.goto(CENTER)
    #     self.write('GAME OVER', align='center', font=("Arial", 20, "normal"))

    def reset(self):
        self.clear()
        if self.score_number > self.high_score:
            self.write_high_score()
        self.__init__()

    def score_point(self):
        self.score_number += 1
        self.draw_score()
