from turtle import Turtle
from random import choice

CAR_COLORS = ['yellow', 'blue', 'green', 'orange', 'purple']

class Car(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.setheading(180)
        self.color(choice(CAR_COLORS))
        self.penup()
        self.shape('square')
        
    def move(self):
        self.forward(self.car_speed)
        
    def set_speed(self, speed: int) -> None:
        self.car_speed = speed
        

class Traffic:
    
    def __init__(self, x_start: int, y_start: int) -> None:
        self.rows = 10
        self.speed = 1
        self.cars_in_row = 1
        self.car_rows = []
        self.x_start = x_start
        self.y_start = y_start
        self.car_size = 20
        self.row_gap = 20
    
    def set_cars(self):
        for row in self.car_rows:
            for car in row:
                car.clear()

        self.car_rows = []
        for i in range(self.rows):
            self.car_rows.append([])
            for _ in range(self.cars_in_row):
                c = Car()
                # TODO make start pos random
                c.goto((self.x_start, (self.car_size + self.row_gap) * i  + self.y_start))
                c.set_speed(self.speed)
                self.car_rows[i].append(c)
    
    def move_cars(self):
        for car_row in self.car_rows:
            for car in car_row:
                car.move()  
        
    def inc_difficulty(self) -> None:
        self.speed += 1
        self.cars_in_row += 1
        
        for i in range(self.rows):
            # TODO adding car to row in separate function
            c = Car()
            # TODO make start pos random
            c.goto((self.x_start, (self.car_size + self.row_gap) * i  + self.y_start))
            self.car_rows[i].append(c)
            for car in self.car_rows[i]:
                car.set_speed(self.speed)
                
