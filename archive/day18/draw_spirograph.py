from random import randint
from turtle import Turtle, Screen, colormode


def random_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return r, g, b


# def draw_circle(t: Turtle,
#                 resolution: int,
#                 step_length: int = 100,
#                 ):
#     angle_per_rotation = 360 / resolution
#     for i in range(resolution):
#         t.forward(step_length)
#         t.left(angle_per_rotation)


def draw_spirograph(t: Turtle,
                    n_circles: int = 30,
                    circle_radius: int = 100,
                    ):
    t.speed("fastest")
    colormode(255)

    pivot_turn_angle_per = 360 / n_circles

    for i in range(n_circles):
        t.left(pivot_turn_angle_per)
        t.color(random_color())
        t.circle(circle_radius)
        # draw_circle(t, circle_resolution, step_length)


tim = Turtle()
draw_spirograph(tim, 100, 100)

screen = Screen()
screen.exitonclick()
