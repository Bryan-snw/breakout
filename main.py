from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreBoard import ScoreBoard
from block import Block
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)
# (42,32,60)
# (49, 47, 50)
screen.bgcolor(49, 47, 50)
screen.title('Breakout Game')

# Disable animation
screen.tracer(0)

# Blocks
level_1 = []
for i in range(0, 770, 70):
    i += 20
    x_pos = -375 + i
    block = Block(x_pos=x_pos, color='yellow')
    level_1.append(block)

level_2 = []
for i in range(0, 770, 70):
    i += 20
    x_pos = -375 + i
    block = Block(x_pos=x_pos,y_pos=30, color='blue')
    level_1.append(block)

level_3 = []
for i in range(0, 770, 70):
    i += 20
    x_pos = -375 + i
    block = Block(x_pos=x_pos, y_pos=60, color='red')
    level_1.append(block)


# Ball
ball = Ball()

# Paddle
paddle = Paddle()

# ScoreBoard
score = ScoreBoard()

screen.listen()
screen.onkey(key='a', fun=paddle.left)
screen.onkey(key='d', fun=paddle.right)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with block
    for blk1 in level_1:
        if ball.distance(blk1) < 25:
            print("Hit")
            ball.bounce_y()
            blk1.disappear()

    for blk2 in level_2:
        if ball.distance(blk2) < 25:
            print("Hit")
            ball.bounce_y()
            blk2.disappear()

    for blk3 in level_3:
        if ball.distance(blk3) < 25:
            print("Hit")
            ball.bounce_y()
            blk3.disappear()

    # Collision with wall
    if ball.ycor() > 280 or ball.distance(paddle) < 30:
        # Bounce
        ball.bounce_y()

    # Collision with paddle
    if ball.xcor() > 370 or ball.xcor() < -380:
        # Bounce
        ball.bounce_x()

    # Ball Fall down
    if ball.ycor() < -275:
        if score.lives == 0:
            game_is_on = False
        else:
            score.decrease_lives()
            ball.reset_position(paddle.xcor())




screen.exitonclick()