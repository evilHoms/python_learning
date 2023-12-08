from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, step):
        super().__init__('square')
        
        self.step = step
        
        self.turtlesize(1, 5)
        self.color('white')
        self.penup()
        self.setheading(90)
        
    def move_up(self):
        self.forward(self.step)
        
    def move_down(self):
        self.back(self.step)
        
    def follow_ball(self):
        pass
    
    def set(self, win_width, left_right):
        x_pos = -win_width / 2 + 40 if left_right == 'left' else win_width / 2 - 40
        self.goto((x_pos, 0))
