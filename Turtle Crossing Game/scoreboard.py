from turtle import Turtle

FONT = ("Courier", 18, "normal")
LEVEL_POSITION = (-220, 260)
MIDDLE = (0,0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.level += 1
        text = f'Level: {self.level}'
        self.clear()
        self.write(text, align='center', font=FONT)

    def game_over(self):
        text = 'Game Over'
        self.goto(MIDDLE)
        self.write(text, align='center', font=FONT)
