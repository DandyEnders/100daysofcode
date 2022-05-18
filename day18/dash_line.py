from turtle import Turtle, Screen


def draw_dash_line(t: Turtle,
                   times: int,
                   move_size: int,
                   ):
    was_pen_down = t.pen()["pendown"]
    for i in range(times):
        t.pendown()
        t.forward(move_size // 2)
        t.penup()
        t.forward(move_size // 2)
    if was_pen_down:
        t.pendown()


if __name__ == "__main__":
    tim = Turtle()
    draw_dash_line(tim, 15, 16)
    screen = Screen()
    screen.exitonclick()
