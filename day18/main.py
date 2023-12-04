import colorgram
from turtle import Turtle, Screen, colormode
from random import randint

GAP = 60
SIZE = 30

colors = colorgram.extract('day18/hirst.jpg', 25)
s = Screen()
t = Turtle()
t.speed('fastest')
t.hideturtle()
colormode(255)

height, width = s.window_height(), s.window_width()
x_start = -width / 2 + SIZE
y_start = height / 2 - SIZE
x_range = int(width / GAP)
y_range = int(height / GAP)

for i in range(x_range):
    for j in range(y_range):
        t.penup()
        t.goto((x_start + i * GAP, y_start - j * GAP))
        rand_color = colors[randint(0, len(colors) - 1)]
        t.dot(SIZE, rand_color.rgb)


s.exitonclick()