from random import randint
from turtle import Turtle, Screen, colormode


def draw_n_gon(t: Turtle,
               n: int):
    assert n >= 3, "n must be 3 or more"
    angle_per_iteration = 360 / n
    colormode(255)
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    for i in range(n):
        t.pencolor(r, g, b)
        t.forward(100)
        t.right(angle_per_iteration)


tim = Turtle()

for i in range(3, 11):
    draw_n_gon(tim, i)

screen = Screen()
screen.exitonclick()
