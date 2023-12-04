# Etch-a-scetch challenge

from turtle import Turtle, Screen

t = Turtle()
s = Screen()

STEP = 10
ANGLE = 10

def forward():
    t.forward(STEP)
    
def back():
    t.back(STEP)
    
def left():
    t.left(ANGLE)
    
def right():
    t.right(ANGLE)
    
def reset():
    t.goto(0, 0)
    t.clear()

s.listen()
s.onkeypress(forward, 'w')
s.onkeypress(left, 'a')
s.onkeypress(right, 'd')
s.onkeypress(back, 's')
s.onkeypress(reset, 'c')
s.exitonclick()