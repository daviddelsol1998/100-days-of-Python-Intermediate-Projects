from turtle import Turtle


class Snake:
    """this class defines the snake look and functionality"""
    def __init__(self):
        self.snake_parts = []
        x = 0

        for i in range(3):
            new_snake_part = Turtle('square')
            new_snake_part.color('white')
            new_snake_part.penup()
            new_snake_part.setx(x)
            x -= 20
            self.snake_parts.append(new_snake_part)

    def move(self):
        """this moves the snake forward"""
        for snake_part in range(len(self.snake_parts) - 1, 0, -1):

            new_x = self.snake_parts[snake_part - 1].xcor()
            new_y = self.snake_parts[snake_part - 1].ycor()
            self.snake_parts[snake_part].goto(new_x, new_y)

        self.snake_parts[0].fd(20)
