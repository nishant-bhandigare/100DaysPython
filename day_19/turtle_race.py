from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Make a bet")

is_race_on = False
colors = ["red", "orange", "yellow", "green","blue", "purple"]
turtles = []

for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x = -230, y = -100 + i*50)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()