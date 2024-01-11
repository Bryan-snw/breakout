from turtle import Turtle

FONT = ('Courier', 36, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-370, 240)
        self.write(f'{self.lives}', align='center', font=FONT)

    def decrease_lives(self):
        self.lives -= 1
        self.update_score_board()
