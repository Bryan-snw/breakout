from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=0.6, stretch_len=3)
        self.color("white")
        self.penup()
        self.goto(0, -240)

    def left(self):
        new_x = self.xcor() - 40
        self.goto(x=new_x, y=self.ycor())

    def right(self):
        new_x = self.xcor() + 40
        self.goto(x=new_x, y=self.ycor())
