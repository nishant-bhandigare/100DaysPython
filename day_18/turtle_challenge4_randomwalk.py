from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")

screen = Screen()
screen.colormode(255)

angles = [0, 90, 180, 270]

for i in range (200):

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    timmy.pencolor(r,g,b)

    timmy.forward(30)
    timmy.right(random.choice(angles))

screen.exitonclick()