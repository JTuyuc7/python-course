# * Day 20

from turtle import Screen
import time
from Snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('_Snake Game_')
screen.tracer(0)

snake = Snake(color='white', shape='square')
food = Food()
score_board = ScoreBoard()
screen.listen()

# ! Methods to move the snake
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
game_is_on = True
# * Snake body
# snake = Turtle(shape='square')
# snake1 = Turtle(shape='square')
# snake2 = Turtle(shape='square')

# for position in starting_positions:
#     new_segment = Turtle(shape='square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)


while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # ! Detect when snake collide with food

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()
        # print('snake should growth xD')

    # ! Detect a collision with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # print('Snake collide with a wall')
        # score_board.game_over()
        # game_is_on = False
        score_board.reset_game()

    # ! Detect when the head collide with any part of the body of the snake
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score_board.game_over()
            # print('collide with your tail *-*-*-*')
            score_board.reset_game()
            snake.reset_snake_game()

    # * Previous implementation
    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    #
    # segments[0].forward(20)


# # * Change color
# snake.color('white')
# snake1.color('white')
# snake2.color('white')
#
# # * position the snake
# snake1.goto(x=-20, y=0)
# snake2.goto(x=-40, y=0)














screen.exitonclick()


