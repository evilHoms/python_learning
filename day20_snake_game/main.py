from turtle import Turtle, Screen

s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.title('Snake Game')

snake_coords = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for coord in snake_coords:
    t = Turtle('square')
    t.color('white')
    t.width(20)
    t.penup()
    t.goto(coord)
    snake.append(t)

game_on = True

while game_on:
    snake_coords.pop()
    snake_coords.insert(0, (snake_coords[0][0] + 20, 0))
    for i in range(len(snake_coords)):
        snake[i].goto(snake_coords[i])
        
    

s.exitonclick()