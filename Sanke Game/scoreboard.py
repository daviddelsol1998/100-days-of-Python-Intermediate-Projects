from turtle import Turtle

TOP = (0, 270)
CENTER = (0,0)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        self.high_score = 0
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(TOP)
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(f'Score:{self.score_number} - High Score:{self.high_score}', align='center', font=("Arial", 20, "normal"))

    # def game_over(self):
    #     self.goto(CENTER)
    #     self.write('GAME OVER', align='center', font=("Arial", 20, "normal"))

    def reset(self):
        if self.score_number > self.high_score:
            self.high_score = self.score_number
        self.score_number = 0

    def score_point(self):
        self.score_number += 1
        self.draw_score()
