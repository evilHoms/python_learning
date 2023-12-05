from turtle import Screen
from snake import Snake

WIDTH = 600
HEIGHT = 600

s = Screen()
s.setup(WIDTH, HEIGHT)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)

snake = Snake(width=WIDTH, height=HEIGHT)

s.update()
game_on = True

s.listen()
s.onkey(snake.turn_left, 'a')
s.onkey(snake.turn_right, 'd')

while game_on:
    if not snake.make_step():
        game_on = False
    s.update()
