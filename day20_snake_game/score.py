from turtle import Turtle
from os import path
from pathlib import Path

dir_path = Path(__file__).parent.resolve()
high_score_path = f'{dir_path}/high_score.txt'

class Score(Turtle):
    
    def __init__(self, height):
        super().__init__()
        
        if not path.exists(high_score_path):
            with open(high_score_path, 'w') as file:
                file.write('0')

        with open(high_score_path) as file:
            self.high_score = int(file.read())
        
        self.score = 0
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
            with open(high_score_path, 'w') as file:
                file.write(str(self.high_score))
            
        self.score = -1
        self.inc()