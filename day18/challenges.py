# Figures challenge

# from turtle import Turtle, Screen
# from random import random

# cursor = Turtle()

# for i in range(3, 360):
#     cursor.color(random(), random(), random())
#     for _ in range(i):
#         cursor.forward(50)
#         cursor.right(360 / i)

# screen = Screen()
# screen.exitonclick()

# Random walk challenge
# from turtle import Turtle, Screen
# from random import random, randint, choice

# c = Turtle()

# def set_random_color():
#     c.color(random(), random(), random())

# def go_forward():
#     set_random_color()
#     c.forward(20)

# def turn_left():
#     set_random_color()
#     c.left(90)
#     c.forward(20)

# def turn_right():
#     set_random_color()
#     c.right(90)
#     c.forward(20)

# def turn_back():
#     c.left(180)
#     c.forward(20)
    
# actions = [go_forward, turn_left, turn_right, turn_back]

# steps = 0
# c.speed(10)
# c.width(3)

# while steps < 1000:
#     steps += 1
#     choice(actions)()
    
# screen = Screen()
# screen.exitonclick()
    
# Spirograph challenge

# from turtle import Turtle, Screen
# from random import random

# c = Turtle()
# c.speed('fastest')
# c.width(2)

# def set_random_color():
#     c.color((random(), random(), random()))
    
# step = 10
    
# for _ in range(int(360 / step)):
#     set_random_color()
#     c.circle(100)
#     c.left(step)
    

# screen = Screen()
# screen.exitonclick()