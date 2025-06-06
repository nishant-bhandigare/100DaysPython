from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def rotate_right():
    timmy.right(10)

def rotate_left():
    timmy.left(10)

def clear_drawing():
    timmy.setposition(0,0)
    timmy.clear()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_right, "d")
screen.onkey(rotate_left, "a")
screen.onkey(clear_drawing, "c")
screen.exitonclick()