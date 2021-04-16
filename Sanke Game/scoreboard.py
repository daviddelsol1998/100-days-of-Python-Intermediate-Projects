from turtle import Turtle

TOP = (0, 270)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(TOP)
        self.draw_score()

    def draw_score(self):
        self.write(f'Score : {self.score_number}', align='center', font=("Arial", 20, "normal"))

    def score_point(self):
        self.score_number += 1
        self.clear()
        self.draw_score()
