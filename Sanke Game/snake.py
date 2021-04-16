from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """this class defines the snake look and functionality"""

    def __init__(self):
        self.snake_parts = []
        self.x = 0

        for _ in range(3):
            self.add_snake_part()

        self.head = self.snake_parts[0]

    def add_snake_part(self):
        new_snake_part = Turtle('square')
        new_snake_part.color('white')
        new_snake_part.penup()
        new_snake_part.setx(self.x)
        self.x -= 20
        self.snake_parts.append(new_snake_part)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move(self):
        """this moves the snake forward"""
        for snake_part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_part - 1].xcor()
            new_y = self.snake_parts[snake_part - 1].ycor()
            self.snake_parts[snake_part].goto(new_x, new_y)

        self.head.fd(20)
