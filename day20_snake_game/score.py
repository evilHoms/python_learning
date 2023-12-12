from turtle import Turtle
from os import path

class Score(Turtle):
    
    def __init__(self, height):
        super().__init__()
        
        if not path.exists('day20_snake_game/high_score.txt'):
            with open('day20_snake_game/high_score.txt', 'w') as file:
                file.write('0')

        with open('day20_snake_game/high_score.txt') as file:
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
            with open('day20_snake_game/high_score.txt', 'w') as file:
                file.write(str(self.high_score))
            
        self.score = -1
        self.inc()