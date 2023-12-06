from turtle import Turtle

class Score(Turtle):
    
    def __init__(self, height):
        super().__init__()
        self.value = 0
        self.hideturtle()
        self.penup()
        self.goto(0, height / 2 - 20)
        self.color('white')
        self.write(f'Score: {self.value}')
        
    def inc(self):
        self.value += 1
        self.clear()
        self.write(f'Score: {self.value}')