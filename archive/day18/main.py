from turtle import Turtle, Screen

timmy = Turtle()
timmy.color("red")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)


screen = Screen()
screen.exitonclick()

import heroes

print(heroes.gen())