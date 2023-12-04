from turtle import Turtle, Screen
from random import randint

t = Turtle()
s = Screen()

S_HEIGHT = 400
S_WIDTH = 400
SIZE = 30
GAP = 30

def one_random_step(turtle):
    step = randint(2, 5)
    turtle.forward(step)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = {}

s.setup(S_WIDTH, S_HEIGHT)
s.screensize(S_WIDTH, S_HEIGHT)

winner = None
bet = ''
while bet not in colors:
    bet = s.textinput('Make a bet', f'Choose a color: ({"/".join(colors)})').lower()
    
index = 0
for color in colors:
    turtles[color] = Turtle()
    turtles[color].shape('turtle')
    turtles[color].width = SIZE
    turtles[color].color(color)
    turtles[color].speed(5)
    turtles[color].penup()
    turtles[color].goto(-S_WIDTH / 2 + SIZE / 2, S_HEIGHT / 2 - (index + 1) * SIZE - index * GAP)
    index += 1
    
while not winner:
    for color in turtles:
        one_random_step(turtles[color])
        if turtles[color].xcor() > S_WIDTH / 2 - SIZE:
            winner = color
            break
      
msg = f'Winner is: {winner}, you loose!'
if winner == bet:
    msg = f'Yeah, you WON!'
    
print(msg)

s.exitonclick()
