from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            # ! Create the car
            new_car = Turtle("square")
            # ! Resize the car
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # ! Penup the car to not draw
            new_car.penup()
            # ! Give the car a random color
            new_car.color(choice(COLORS))
            # ! Position the car to a random position
            random_y = randint(-260, 260)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

