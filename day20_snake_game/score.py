from turtle import Turtle

class Score(Turtle):
    
    def __init__(self, height):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, height / 2 - 20)
        self.color('white')
        self.write(f'Score: {self.score} High Score: {self.high_score}')
        
    def inc(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}')
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
        self.score = -1
        self.inc()