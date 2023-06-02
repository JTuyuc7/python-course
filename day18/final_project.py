# * Final project Day 18

# import colorgram
import turtle as turtle_module
import random

# ? Get all colors using cologram
# colors = colorgram.extract('img2.jpeg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple_color = (r, g, b)
#     rgb_colors.append(new_tuple_color)
#
# print(rgb_colors, '#! list of colors')

tom = turtle_module.Turtle()
screen = turtle_module.Screen()
tom.penup()
tom.hideturtle()
screen.colormode(255)

colors_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
               (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
               (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
               (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187),
               (151, 206, 220)]  # ! list of colors

tom.setheading(225)
tom.forward(380)
tom.setheading(0)
number_of_dots = 120

for dot_count in range(1, number_of_dots + 1):
    tom.dot(20, random.choice(colors_list))
    tom.forward(50)

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)








screen.exitonclick()