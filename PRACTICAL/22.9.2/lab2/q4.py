import turtle
import math

c = input("Please enter the center of the circle: ")
r = float(input("Please enter the radius of the cirlce: "))

c = c.replace(" ", "").split(",")
x = int(c[0])
y = int(c[1])

a = math.pi * (r * r)

t = turtle.Turtle()

t.pu()
t.goto(x, y - r)
t.pd()

t.circle(r)

t.pu()
t.goto(x, y)
t.pd()

t.write(a)

turtle.done()