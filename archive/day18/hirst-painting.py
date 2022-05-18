# import colorgram
#
# colors = colorgram.extract("./img/20_001.jpg", 10)
#
# rgbs = []
# for color in colors:
#     rgbs.append(tuple([*color.rgb]))
#
# print(rgbs)

# extracted
# [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
import random
from random import randint
from turtle import Turtle, Screen, colormode

COLOR_LIST = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85)]


def random_color():
    return random.choice(COLOR_LIST)


def hirst_painting(t: Turtle,
                   square_size: int = 10,
                   distance_between_dots: int = 10,
                   dot_size: int = 10,
                   ):
    last_anchor_pos = t.pos()
    was_pen_down = t.isdown()
    t.penup()
    colormode(255)
    t.speed("fastest")
    for row in range(square_size):
        for col in range(square_size):
            dot_color = random_color()
            t.dot(dot_size, dot_color)
            t.forward(distance_between_dots)
        t.setx(last_anchor_pos[0])
        t.sety(last_anchor_pos[1] + distance_between_dots)
        last_anchor_pos = t.pos()

    if was_pen_down:
        t.pendown()


tim = Turtle()
hirst_painting(tim, 10, 30, 15)

screen = Screen()
screen.exitonclick()
