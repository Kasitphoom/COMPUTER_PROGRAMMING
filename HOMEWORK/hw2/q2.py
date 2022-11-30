import turtle
import random

t = turtle.Turtle()

t.screen.bgcolor("#070024")

t.pensize(2)
t.speed(0)

# draw a ground
t.fillcolor("#fce3a4")
t.begin_fill()
t.circle(-100000)
t.end_fill()

t.pencolor("white")
t.pu()
t.goto(0, 0)
t.setheading(0)

# bottom body
t.goto(-250, 66.99)
t.rt(30)
t.pd()

t.circle(500, 60)

# draw right legs
cPos = t.pos()
cHead = t.heading()

t.setheading(270)
t.fd(80)

t.pu()
t.lt(90)
t.bk(20)
t.pd()
t.fillcolor("#bdbfbf")
t.begin_fill()
for i in range(2):
    t.fd(40)
    t.rt(90)
    t.fd(5)
    t.rt(90)
t.end_fill()


t.pu()
t.goto(cPos)
t.setheading(cHead)
t.pd()

# draw top part
t.circle(30,180)

t.rt(90)

t.fillcolor("#bdb6bf")
t.begin_fill()
t.circle(253, 120.5)
t.end_fill()
t.rt(90)
topPos = t.pos()
topHead = t.heading()
t.circle(30,180)

# draw left legs
cPos = t.pos()
cHead = t.heading()
t.setheading(270)
t.fd(80)

t.pu()
t.lt(90)
t.bk(20)
t.pd()
t.fillcolor("#bdbfbf")
t.begin_fill()
for i in range(2):
    t.fd(40)
    t.rt(90)
    t.fd(5)
    t.rt(90)
t.end_fill()
    
t.pu()
t.goto(cPos)
t.setheading(cHead)

# draw a line to a house
t.pencolor("black")

t.goto(-10,1)
t.rt(120)

t.pd()
t.fd(500)
t.pu()

t.goto(10,1)
t.lt(120)

t.pd()
t.fd(500)
t.pu()
t.pencolor("white")

# draw a door
t.goto(-10,1)
t.fillcolor("#bdbfbf")
t.begin_fill()
t.pd()
t.setheading(90)
t.fd(30)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(30)
t.end_fill()

# draw a second floor
t.pu()
t.goto(topPos)
t.setheading(topHead + 180)
t.pd()
t.fillcolor("#bdb6bf")
t.begin_fill()
t.circle(440, 60)
t.end_fill()

# draw a window
t.pu()
t.goto(topPos)
t.setheading(90)
t.bk(30)

t.fillcolor("#87ddff")

for i in range(2):
    t.pd()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.pu()
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(20)
    t.lt(180)

for i in range(2):
    t.pd()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.pu()
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(10)
    t.lt(180)

t.goto(89.30, 37.03)

for i in range(2):
    t.pd()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.pu()
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(10)
    
t.fd(8)
    
for i in range(2):
    t.pd()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.pu()
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(27)
t.end_fill()

# draw a star
t.pensize(1)
for i in range(70):
    x = random.randint(-1000, 1000)
    y = random.randint(0, 500)
    
    if x in range(-300, 300) and y in range(0, 270):
        continue
    
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor("white")
    t.circle(2)
    t.end_fill()

turtle.done()