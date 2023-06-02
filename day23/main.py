import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# ! Define the first turtle player
player = Player()

# ! Define the list of cars
car_manager = CarManager()

# ! Define the scoreboard
scoreboard = Scoreboard()

# ! Move the turtle up
screen.listen()
screen.onkey(player.go_up, "Up")

# ! Move the turtle down
# screen.listen()
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # ! Create all cars
    car_manager.create_car()
    # ! Move the cars on the x axis
    car_manager.move_cars()

    # ! Detect when the turtle hits a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # ! return the turtle back to the begin if a successful cross
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    # else:
    #     game_is_on = False

screen.exitonclick()
