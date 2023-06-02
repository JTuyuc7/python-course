# * Turtle Race

from turtle import Turtle, Screen
import random

screen = Screen()

# * Set the dimensions of the screen
screen.setup(width=500, height=400)

# * prompt to the user makes a bet
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? enter a color: ')

# * list of colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
is_race_on = False
all_turtles = []
# * Move the first turtle to the beginning of the screen
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You got it correct, the winning is {winning_color}')
            else:
                print(f'You lost, the winner is {winning_color}')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

