from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.8, 0.8)
        self.penup()
        self.goto(0, -220)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.081

    def reset_position(self, paddle_position):
        self.move_speed = 0.09
        self.goto(paddle_position, -220)
        self.bounce_y()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # self.move_speed *= 0.9
