from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

WIDTH = 800
HEIGHT = 600
PADDLE_STEP = 20
BALL_SPEED = (10, 11)

def set_screen():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor('black')
    return screen

s = set_screen()
s.tracer(0)

player = Paddle(WIDTH, 'left', PADDLE_STEP)
comp = Paddle(WIDTH, 'right', PADDLE_STEP)

ball = Ball(BALL_SPEED)

s.listen()

s.onkeypress(player.move_up, 'w')
s.onkeypress(player.move_down, 's')

game_on = True

while game_on:
    ball.move()
    comp.follow_ball()
    
    if ball.ycor() >= HEIGHT / 2 - 10 or ball.ycor() <= -HEIGHT / 2 + 10:
        ball.bounce_y()
    
    if ball.distance(comp) <= 50 and ball.xcor() >= WIDTH / 2 - 60:
        ball.bounce_x_to_left()
        
    if ball.distance(player) <= 50 and ball.xcor() <= -WIDTH / 2 + 60:
        ball.bounce_x_to_right()
        
    if ball.xcor() >= WIDTH / 2 or ball.xcor() <= -WIDTH / 2:
        print('score')

    s.update()    
    sleep(.04)
    

s.exitonclick()
