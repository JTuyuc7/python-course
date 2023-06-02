# * Class to create the Pad
from turtle import Turtle

POSITIONS = [()]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # paddle = Turtle(shape='square')
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        # game_is_on = True

        self.goto(position)

    def go_up(self):
        if self.ycor() > 220:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() < -210:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)