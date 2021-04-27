from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game with Turtle')
screen.tracer(0)

game_is_on = True

# todo: setup paddle player
right_paddle = Paddle(x=380, y=0)

# todo setup cpu
left_paddle = Paddle(x=-390, y=0)

screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')



while game_is_on:
    screen.update()

screen.exitonclick()
