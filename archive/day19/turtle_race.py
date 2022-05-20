from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

is_race_on = False

for i, colour in enumerate(colours):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=i * 50 - ((len(colours) - 1) / 2) * 50)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You have won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You have lost... The {winning_colour} turtle is the winner!")
            is_race_on = False
            break
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
