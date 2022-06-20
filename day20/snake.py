from turtle import Turtle

MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    def __init__(self, init_length=3):
        self._segments = []
        for i in range(init_length):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.setpos(i * -MOVE_DISTANCE, 0)
            self._segments.append(new_turtle)
        self.head = self._segments[0]

    def move(self):
        for seg_num in range(len(self._segments) - 1, 0, -1):
            next_seg = self._segments[seg_num - 1]
            new_x = next_seg.xcor()
            new_y = next_seg.ycor()
            previous_seg = self._segments[seg_num]
            previous_seg.goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)