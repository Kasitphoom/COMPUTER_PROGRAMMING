import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.tracer(0,0)
def cross(width, times):
    if times == 0:
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        t.dot(30, hexadecimal[0])
        return
    else:
        for i in range(4):
            t.fd(width)
            cross(width/2,times-1)
            t.rt(180)
            t.fd(width)
            t.lt(90)

cross(100, 7)
turtle.update()
turtle.done()