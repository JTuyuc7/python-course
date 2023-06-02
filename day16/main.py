# * OOP (Object Oriented Programming)

# * Procedural Programming

# import turtle
#
# timmy = turtle.Turtle()
# my_screen = turtle.Screen()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# # print(timmy)
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

pokemon_name = ['Pikachu', 'Squirrel', 'Charmander']
pokemon_type = ['Electric', 'Water', 'Fire']

table.add_column('Pokemon Name', pokemon_name)
table.add_column('Type', pokemon_type)

table.align = "l"

print(table)
















