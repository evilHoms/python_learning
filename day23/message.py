from turtle import Turtle

class Message(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        
        self.level = 1
        self.msg_pos = pos
        
        self.penup()
        self.hideturtle()
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over')
        
    def print_level(self):
        self.clear()
        self.goto(self.msg_pos)
        self.write(f'Level: {self.level}')
        
    def lvl_up(self):
        self.level += 1
        
