import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('day18/hirst.jpg', 25)
s = Screen()
t = Turtle()
t.speed('fastest')

height, width = s.window_height(), s.window_width()
t.penup()
t.goto((-100, -100))
print(height, width)


s.exitonclick()