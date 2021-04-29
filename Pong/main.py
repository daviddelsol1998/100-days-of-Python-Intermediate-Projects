from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game with Turtle')
screen.tracer(0)

game_is_on = True

ball = Ball()
score = Scoreboard()

# todo: setup paddle player
right_paddle = Paddle(x=380, y=0)

# todo setup cpu
left_paddle = Paddle(x=-390, y=0)

screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.goto(x=0,y=0)
        ball.bounce_x()
        score.l_point()

    if ball.xcor() < -380:
        ball.goto(x=0, y=0)
        ball.bounce_y()
        score.r_point()

screen.exitonclick()
