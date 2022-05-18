import random
from turtle import Turtle, Screen, colormode


def random_walk(t: Turtle,
                steps: int,
                distance_per: int = 50,
                width: int = 10,
                speed: int = 0,
                ):
    assert steps > 0
    assert distance_per > 0
    assert width > 0
    assert 10 >= width >= 0

    directions = [90, 180, 0, -90]
    colormode(255)
    t.width(width)
    t.speed(speed)
    for i in range(steps):
        next_angle = random.choice(directions)
        t.color(random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
                )
        t.right(next_angle)
        t.forward(distance_per)


tim = Turtle()
random_walk(tim, 50)

screen = Screen()
screen.exitonclick()
