from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

is_game_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
b = Ball()
s = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    b.move()

    #Collision with walls
    if b.ycor() >= 280 or b.ycor() <= -280:
        b.bounce_y()

    #Collision with right paddle
    if b.distance(r_paddle) < 50 and b.xcor() > 330:
        b.bounce_x()
        b.fast()

    #Collision with left paddle
    if b.distance(l_paddle) < 50 and b.xcor() < -330:
        b.bounce_x()
        b.fast()

    #Right paddle misses the ball
    if b.xcor() > 400:
        b.reset_position()
        b.reset_speed()
        s.l_point()

    #Left paddle misses the ball
    if b.xcor() < -400:
        b.reset_position()
        b.reset_speed()
        s.r_point()

screen.exitonclick()