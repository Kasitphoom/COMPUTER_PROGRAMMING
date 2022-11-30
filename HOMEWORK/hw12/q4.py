import turtle
from abc import ABC, abstractmethod

turtle.pensize(30)

class Char:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def draw(x, y):
        pass
    
    @abstractmethod
    def getWidth():
        pass

class Char0(Char):
    def __init__(self) -> None:
        super().__init__()

    def draw(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.pensize(30)
        turtle.circle(30)
        
    def getWidth():
        return 60
    
class Char1(Char):
    def __init__(self) -> None:
        super.__init__()
    
    def draw( x, y):
        # draw number 1 in turtle
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.fd(50)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(20)
        turtle.rt(90)
        turtle.fd(100)
        turtle.lt(90)
        turtle.fd(30)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(20)
        turtle.rt(90)
        turtle.fd(90)
        turtle.rt(90)
        turtle.fd(20)
        turtle.lt(90)
        turtle.fd(10)
    
    def getWidth():
        return 50
        
class Char2(Char):
    def __init__(self) -> None:
        pass
    
    def draw(x, y):
        # draw number 2 in turtle
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.fd(50)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(40)
        turtle.rt(175)
        turtle.circle(40, 180)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.circle(-30, 200)
        turtle.lt(90)
        turtle.fd(20)
    
    def getWidth():
        return 50
    
class Char3(Char):
    def __init__(self) -> None:
        pass
    
    def draw(x, y):
        # draw number 3 in turtle
        turtle.pensize(30)
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.circle(40, 180)
        turtle.rt(180)
        turtle.circle(40, 180)
    
    def getWidth():
        return 40
        
class Char4(Char):
    def __init__(self) -> None:
        super().__init__()

    def draw(x, y):
        # draw number 4 in turtle
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.setheading(90)
        turtle.fd(100)
        turtle.bk(50)
        turtle.rt(90)
        turtle.fd(30)
        turtle.bk(100)
        turtle.lt(90)
        turtle.fd(50)
    
    def getWidth():
        return 100
    
class Char5(Char):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(x, y):
        # draw number 5 in turtle
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.circle(40, 180)
        turtle.rt(90)
        turtle.fd(40)
        turtle.rt(90)
        turtle.fd(40)
    
    def getWidth():
        return 40

class Char6(Char):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(x, y):
        # draw number 6 in turtle
        x, y
        turtle.up()
        turtle.goto(x, y - 60)
        turtle.setheading(-90)
        turtle.down()
        
        turtle.fd(60)
        turtle.lt(90)
        turtle.fd(60)
        turtle.lt(90)
        turtle.fd(60)
        turtle.lt(90)
        turtle.fd(60)
        turtle.rt(90)
        turtle.fd(60)
        turtle.rt(90)
        turtle.fd(60)
    
    def getWidth():
        return 60

class Char7(Char):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(x, y):
        # draw number 7 in turtle
        turtle.setheading(90)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.fd(100)
        turtle.lt(90)
        turtle.fd(60)
    
    def getWidth():
        return 60
    
class Char8(Char):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(x, y):
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.circle(-50)
        turtle.circle(50)
    
    def getWidth():
        return 100

class Char9(Char):
    def __init__(self) -> None:
        super().__init__()
        
    def draw(x, y):
        # draw number 9 in turtle
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.circle(50)
        turtle.circle(50, 90)
        turtle.bk(100)
    
    def getWidth():
        return 100

def drawNum(x):
    xpos = 0
    num_dict = {
        '0': Char0,
        '1': Char1,
        '2': Char2,
        '3': Char3,
        '4': Char4,
        '5': Char5,
        '6': Char6,
        '7': Char7,
        '8': Char8,
        '9': Char9
    }
    
    for i in x:
        num_dict[i].draw(xpos, 0)
        xpos += num_dict[i].getWidth()
    
drawNum("987965432100324987")

# Char1.draw(100, 0)    