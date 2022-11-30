import turtle

from abc import ABC, abstractmethod


class TwoDShape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    
    @abstractmethod
    def draw(self):
        pass
    
class Line(TwoDShape):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def draw(self):
        t = turtle.Turtle()
        t.pu()
        t.goto(self.coor1)
        t.pd()
        t.goto(self.coor2)
        t.pu()
        

class Rectangle(TwoDShape):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def draw(self):
        t = turtle.Turtle()
        t.pu()
        t.goto(self.coor1)
        t.pd()
        t.goto(self.coor2[0], self.coor1[1])
        t.goto(self.coor2)
        t.goto(self.coor1[0], self.coor2[1])
        t.goto(self.coor1)
        t.pu()

class Circle(TwoDShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        t = turtle.Turtle()
        t.pu()
        t.goto(self.x, self.y - self.radius)
        t.pd()
        t.circle(self.radius)
        t.pu()


