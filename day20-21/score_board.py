# * Score board class

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.high_score = 0
        self.score = 0
        self.color('white')
        self.goto(0, 240)
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over :(', align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
