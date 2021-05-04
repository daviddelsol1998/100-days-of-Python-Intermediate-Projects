from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)
        if self.ycor() > self.finish_line:
            self.goto(STARTING_POSITION)
