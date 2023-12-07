from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, speed):
        super().__init__()
        
        self.ball_speed = speed
        self.dir = [-1, 1]
        
        self.penup()
        self.color('blue')
        self.shape('circle')
        self.goto((0, 0))
        
    def move(self):
        x_pos = self.xcor() + self.ball_speed[0] * self.dir[0]
        y_pos = self.ycor() + self.ball_speed[1] * self.dir[1]
        self.goto(x_pos, y_pos)
        
    def bounce_y(self):
        self.dir[1] *= -1
            
    def bounce_x_to_left(self):
        self.dir[0] = -1
        
    def bounce_x_to_right(self):
        self.dir[0] = 1
        
    
