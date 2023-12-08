from turtle import Turtle

class Player(Turtle):
    
    def __init__(self, start_pos, step = 40):
        super().__init__()
        
        self.start_pos = start_pos
        self.step_size = step
        
        self.setheading(90)
        self.penup()
        self.color('black')
        self.shape('turtle')
        
    def step(self):
        self.forward(self.step_size)
        
    def to_start(self):
        self.goto(self.start_pos)
