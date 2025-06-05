from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()

shapes = 8
side_count = 3
angles_interior = [60, 90, 108, 120, 128.57, 135, 140, 144]
angles_exterior = [120, 90, 72, 60, 51.43, 45, 40, 36]
angles_index = 0

screen.colormode(255)

for _ in range(shapes):

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r,g,b)

    angle = 360/side_count

    for i in range(side_count):
        timmy.forward(100)
        # timmy.right(angles_exterior[angles_index])
        timmy.right(angle)

    side_count+=1
    angles_index+=1


screen.exitonclick()