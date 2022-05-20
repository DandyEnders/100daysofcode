from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def forward():
    tim.forward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


def back():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="s", fun=back)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
