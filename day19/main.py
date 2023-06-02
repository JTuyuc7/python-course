# * Day 19 understand more about turtles

from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


# * Define a function
def move_forwards():
    tom.forward(10)


def move_left():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)


def move_right():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)


def move_backwards():
    tom.backward(10)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()  # * Listen to key events using the keyboard


screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()