from turtle import Turtle
from random import choice, randint

CAR_COLORS = ['yellow', 'blue', 'green', 'orange', 'purple']

class Car(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.setheading(180)
        self.turtlesize(1, 2)
        self.color(choice(CAR_COLORS))
        self.penup()
        self.shape('square')
        
    def move(self):
        self.forward(self.car_speed)
        
    def set_speed(self, speed: int) -> None:
        self.car_speed = speed
        
    def check_collision(self, t: Turtle) -> bool:
        if (self.xcor() + 20 > t.xcor() - 10 and self.xcor() - 20 < t.xcor() + 10
            and self.ycor() + 10 > t.ycor() - 10 and self.ycor() - 10 < t.ycor() + 10):
            return True
        return False
        

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
        
    def new_car(self, row_number, start_point):
        c = Car()
        rand_x_offset = randint(0, self.x_start * 2)
        c.goto((start_point + rand_x_offset, (self.car_size + self.row_gap) * row_number  + self.y_start))
        c.set_speed(self.speed)
        return c
    
    def set_cars(self):
        for row in self.car_rows:
            for car in row:
                car.clear()

        self.car_rows = []
        for i in range(self.rows):
            self.car_rows.append([])
            for _ in range(self.cars_in_row):
                self.car_rows[i].append(self.new_car(i, -self.x_start))
    
    def move_cars(self):
        for car_row in self.car_rows:
            for car in car_row:
                car.move()
                if car.xcor() < -self.x_start:
                    rand_x_offset = randint(0, self.x_start * 2)
                    car.back(self.x_start * 2 + rand_x_offset)
        
    def inc_difficulty(self) -> None:
        self.speed += 1
        self.cars_in_row += 1
        
        for i in range(self.rows):
            self.car_rows[i].append(self.new_car(i, self.x_start))
            for car in self.car_rows[i]:
                car.set_speed(self.speed)
                
