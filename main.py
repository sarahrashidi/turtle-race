import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_input = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color!(Red,Orange,Yellow,Green,Blue,Purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []


for all_turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[all_turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[all_turtles])
    turtles.append(new_turtle)


if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        print(turtle.color)
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
