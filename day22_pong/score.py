from turtle import Turtle

class Score(Turtle):
    
    def __init__(self, pos_y):
        super().__init__()
        
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto((20, pos_y))
        
        self.score = [0, 0]

        self.print()
        
    def print(self):
        self.clear()
        self.write(f'{self.score[0]} : {self.score[1]}')
        
    def point_to_p1(self):
        self.score[0] += 1
        
    def point_to_p2(self):
        self.score[1] += 1
