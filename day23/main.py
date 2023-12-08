from turtle import Screen
from time import sleep
from message import Message
from player import Player
from traffic import Traffic

WIDTH = 600
HEIGHT = 600

Y_BORDER = HEIGHT / 2
X_BORDER = WIDTH / 2

PLAYER_START = (0, -Y_BORDER + 20)
MESSAGE_POS = (-WIDTH / 2 + 20, Y_BORDER -20)

s = Screen()
s.setup(WIDTH, HEIGHT)
s.tracer(0)

m = Message(MESSAGE_POS)
p = Player(PLAYER_START)
m.print_level()
p.to_start()

s.listen()
s.onkey(p.step, 'w')

t = Traffic(X_BORDER, -Y_BORDER + 60)
t.set_cars()

game_on = True

while game_on:
    sleep(0.01)
    s.update()
    
    t.move_cars()
    # TODO collision check
    
    if p.ycor() >= Y_BORDER:
        m.lvl_up()
        m.print_level()
        p.to_start()
        t.inc_difficulty()
        
