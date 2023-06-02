# * Python TURTLE

from turtle import Turtle, Screen
import random
timmy_turtle = Turtle()

timmy_turtle.shape('triangle')
timmy_turtle.color('red')
timmy_turtle.speed('fastest')
screen = Screen()

screen.colormode(255)
# timmy_turtle.speed(1)

#* ---------------------------------------------

# for _ in range(4):
#     timmy_turtle.forward(200)
#     timmy_turtle.right(90)

#* ---------------------------------------------

# timmy_turtle.forward(100)
# timmy_turtle.penup()
# timmy_turtle.pensize(5)

#* ---------------------------------------------

# for _ in range(4): # Draw a dashed line
#     timmy_turtle.forward(50)
#     timmy_turtle.penup()
#     timmy_turtle.forward(50)
#     timmy_turtle.pendown()

#* ---------------------------------------------

num_sides = 7
color_list = ['#B3533F', '#709920', '#203A99', '#680C63', '#6F2947', '#45563C', '#D75E2E', '#C3E80B']

# while num_sides > 2:
#     timmy_turtle.color(random.choice(color_list))
#     for n in range(num_sides):
#         angle = 360 / num_sides
#         timmy_turtle.forward(100)
#         timmy_turtle.right(angle)
#     num_sides -= 1

#* ---------------------------------------------

# def draw_shape(n_sides, color):
#     timmy_turtle.color(color)
#     angle = 360 / n_sides
#     for _ in range(n_sides):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     color = random.choice(color_list)
#     draw_shape(shape_side_n, color)

#* ---------------------------------------------

# directions = [0, 90, 180, 270]
# timmy_turtle.pensize(5)
#
#
# def random_color():
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#
#     random_color_tuple = (r, g, b)
#     return random_color_tuple
#
#
# for _ in range(100):
#
#     timmy_turtle.color(random_color())
#     timmy_turtle.forward(50)
#     timmy_turtle.setheading(random.choice(directions))


#* ---------------------------------------------

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    random_color_tuple = (r, g, b)
    return random_color_tuple

r = 100
timmy_turtle.width(2)


def draw_siprgraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_turtle.color(random_color())
        timmy_turtle.circle(r)

        current_heading = timmy_turtle.heading()
        timmy_turtle.setheading( current_heading + size_of_gap)


draw_siprgraph(5)

print(timmy_turtle.heading())



screen.exitonclick()
