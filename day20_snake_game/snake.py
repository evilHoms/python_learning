from turtle import Turtle
from time import sleep

STEP = 20

class Snake():
    def __init__(self, width, height, pos=(0, 0), length=3):
        self.pos = pos
        self.length = length
        self.heading = (STEP, 0)
        self.can_turn = True
        self.win_width = width
        self.win_height = height
        self.should_grow = False
        self.score = 0
        self.snake = []
        self.reset()
            
    def make_step(self, delay=.5):
        if self.should_grow:
            self.should_grow = False
        else:
            self.coords.pop()

        self.coords.insert(0, (self.coords[0][0] + self.heading[0], self.coords[0][1] + self.heading[1]))
        for i in range(len(self.snake)):
            self.snake[i].goto(self.coords[i])

            if i != 0 and self.check_tail(i):
                return False
            if i == 0 and self.check_border():
                return False
            
        if len(self.coords) > len(self.snake):
            self.grow(self.coords[len(self.coords) - 1])
            
        sleep(delay)
        self.check_border()

        self.can_turn = True
        return True
    
    def grow(self, coord):
        t = Turtle('square')
        t.color('white')
        t.shapesize(STEP / 20)
        t.penup()
        t.goto(coord)
        self.snake.append(t)
        
    def turn_left(self):
        if not self.can_turn:
            return
        if self.heading[0] == STEP:
            self.heading = (0, STEP)
        elif self.heading[1] == STEP:
            self.heading = (-STEP, 0)
        elif self.heading[0] == -STEP:
            self.heading = (0, -STEP)
        else:
            self.heading = (STEP, 0)
        self.can_turn = False
            
    def turn_right(self):
        if not self.can_turn:
            return
        if self.heading[0] == STEP:
            self.heading = (0, -STEP)
        elif self.heading[1] == STEP:
            self.heading = (STEP, 0)
        elif self.heading[0] == -STEP:
            self.heading = (0, STEP)
        else:
            self.heading = (-STEP, 0)
        self.can_turn = False
        
    def check_border(self):
        if (self.coords[0][0] < -self.win_width / 2 or self.coords[0][0] > self.win_width / 2
            or self.coords[0][1] < -self.win_height / 2 or self.coords[0][1] > self.win_height / 2):
            return True
    
    def check_tail(self, i):
        if self.coords[i][0] == self.coords[0][0] and self.coords[i][1] == self.coords[0][1]:
            return True
        
    def eat(self):
        self.score += 1
        self.should_grow = True
        
    def reset(self):
        self.coords = [self.pos]
        t = Turtle()
        t.clear()
        if self.snake:
            for seg in self.snake:
                seg.goto(1000, 1000)
        self.snake.clear()
        last_pos_x = self.pos[0]

        for _ in range(1, self.length):
            last_pos_x -= STEP
            self.coords.append((last_pos_x, self.pos[1]))
            
        for coord in self.coords:
            self.grow(coord)
            
        self.head = self.snake[0]