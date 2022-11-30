import turtle
import q4 as test4
class Square(test4.TwoDShape):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def draw(self):
        t = turtle.Turtle()
        t.pu()
        t.goto(self.x - (self.x / 2), self.y + (self.y / 2))
        t.pd()
        for i in range(4):
            t.fd(self.size)
            t.rt(90)
        t.pu()