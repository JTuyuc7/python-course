# * Pong Game

from turtle import Screen
from paddle import Paddle
from score_board import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')
screen.tracer(0)

# ! Refactor the code to use Classes
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score_board = ScoreBoard()

# paddle = Turtle(shape='square')
# paddle.penup()
# paddle.color('white')
# paddle.shapesize(stretch_wid=5, stretch_len=1)
game_is_on = True

# paddle.goto(x=370, y=0)
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # ! Detect when collides with top or bottom sides
    if ball.ycor() > 290 or ball.ycor() < -280:
        print('touch the top or bottom side')
        ball.bounce_y()

    # ! Detect when collide with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # ! Detect when the ball pass the r paddle
    if ball.xcor() > 390:
        ball.reset_position()
        score_board.l_point()

    # ! Detect when the bal pass the l paddle
    if ball.xcor() < -390:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()