from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# for i in range (1,50):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.right(10)

def draw_spirograoh(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograoh(5)

screen.exitonclick()