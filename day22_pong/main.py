from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
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

player = Paddle(PADDLE_STEP)
comp = Paddle(PADDLE_STEP)
score = Score(HEIGHT / 2 - 20)

player.set(WIDTH, 'left')
comp.set(WIDTH, 'right')

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
        
    if ball.xcor() > 0 and ball.ycor() > comp.ycor() + 40:
        comp.move_up()
    elif ball.xcor() > 0 and  ball.ycor() < comp.ycor() - 40:
        comp.move_down()
        
    if ball.xcor() >= WIDTH / 2:
        score.point_to_p1()
        score.print()
        ball.reset()
        player.set(WIDTH, 'left')
        comp.set(WIDTH, 'right')
        sleep(2)
        
    if  ball.xcor() <= -WIDTH / 2:
        score.point_to_p2()
        score.print()
        ball.reset()
        player.set(WIDTH, 'left')
        comp.set(WIDTH, 'right')
        sleep(2)

    s.update()    
    sleep(.04)
    

s.exitonclick()
