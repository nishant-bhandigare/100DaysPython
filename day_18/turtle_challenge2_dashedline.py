from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

for i in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()