from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

PADDLE_POSITIONS = [(350, 0), (-350,0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) #turns off the animation, but if we turn off the animation, we have to manually update the screen

r_paddle = Paddle(PADDLE_POSITIONS[0])
l_paddle = Paddle(PADDLE_POSITIONS[1])

ball = Ball()
scoreboard  = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    #detecting collision with left and right wall / (going out of bounds)
    # if ball.xcor() > 380 or ball.xcor() <-380:
    #     # ball.bounce_x()
    #     game_is_on = False

    #detecting collsion with paddle
    # if ball.xcor() == 340 and ball.ycor() <= r_paddle.ycor() + 50 and ball.ycor() >= r_paddle.ycor() -50:
    #     ball.bounce_x()

    if ball.distance(r_paddle) <50 and ball.xcor()> 320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    #detect L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()