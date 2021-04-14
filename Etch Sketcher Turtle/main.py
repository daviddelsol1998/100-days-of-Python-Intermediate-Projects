from turtle import Turtle, Screen


# todo set up turtle
tim = Turtle()


# todo move forward function
def forward():
    tim.fd(10)


# todo move backward function
def backward():
    tim.bk(10)


# todo turn right function
def right():
    tim.rt(10)


# todo turn left function
def left():
    tim.lt(10)


# todo set up screen
screen = Screen()
screen.title('Day 19')


# todo set up clear function
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# todo setup keys and call functions
screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='d', fun=right)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
