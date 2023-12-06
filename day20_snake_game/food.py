from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self, width, height, size):
        super().__init__('circle')
        self.penup()
        self.shapesize(size / 20)
        self.color('blue')
        self.speed('fastest')
        self.win_width = width
        self.win_height = height
        
    def to_rand_pos(self):
        rand_x = randint(-self.win_width / 2 + 20, self.win_width / 2 - 20)
        rand_y = randint(-self.win_height / 2 + 20, self.win_height / 2 - 20)
        self.goto(rand_x, rand_y)