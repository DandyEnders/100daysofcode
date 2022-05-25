from turtle import Turtle


class Snake():
    def __init__(self, init_length=3):
        self._segments = []
        for i in range(init_length):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.setpos(i * -20, 0)
            self._segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self._segments) - 1, 0, -1):
            next_seg = self._segments[seg_num - 1]
            new_x = next_seg.xcor()
            new_y = next_seg.ycor()
            previous_seg = self._segments[seg_num]
            previous_seg.goto(new_x, new_y)
        self._segments[0].forward(20)
        self._segments[0].left(90)
