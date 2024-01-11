from turtle import Turtle


class Block(Turtle):
    def __init__(self, x_pos, y_pos=0, color='yellow'):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=3)
        self.color(color)
        self.penup()
        self.goto(x=x_pos, y=y_pos)

    def disappear(self):
        self.goto(450, 0)
