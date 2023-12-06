from turtle import Screen
from snake import Snake
from food import Food
from score import Score

WIDTH = 600
HEIGHT = 600
SPEED = 10
FOOD_SIZE = 10

s = Screen()
s.setup(WIDTH, HEIGHT)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)

food = Food(WIDTH, HEIGHT, FOOD_SIZE)
snake = Snake(WIDTH, HEIGHT)
score = Score(HEIGHT)

food.to_rand_pos()

s.update()
game_on = True

s.listen()
s.onkey(snake.turn_left, 'a')
s.onkey(snake.turn_right, 'd')

while game_on:
    if not snake.make_step(1 / SPEED):
        game_on = False
    s.update()
    
    if snake.head.distance(food) < FOOD_SIZE * 1.5:
        snake.eat()
        food.to_rand_pos()
        score.inc()
