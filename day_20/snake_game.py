from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #done in part 2 to avoid caterpillar motion of the snake (tracer is turned off (CRT display))


#part 1: creating the snake body

# turtles = []
# for i in range(3):
#     new_turtle = Turtle()
#     new_turtle.shape("square")
#     new_turtle.color("white")
#     new_turtle.goto(x = -20*i , y = 0)
#     turtles.append(new_turtle)

segments = []
starting_positions = [(0,0), (-20,0), (-40,0)]
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup() #done in part 2
    new_segment.goto(position)
    segments.append(new_segment)
# screen.update() #done in part 2, once all segments take position update the screen


#part 2: animating the snake segments on screen ie. moving the snake

game_is_on =True
while game_is_on:
    screen.update() #done in part 2: once all segments move forward then update the screen
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

# new plan, instead of seg1 moves forward then seg2 moves forward, then seg3 moves forward
# we do: seg 3 moves at position of seg2, seg2 moves at position of seg 1, seg 1 moves forward
    
    # for seg_num in range(start=len(segments)-1 , stop=0 , step= -1):
    for seg_num in range(len(segments)-1 , 0 , -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()