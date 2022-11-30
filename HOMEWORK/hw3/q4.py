# draw an olympic rings with colors
import turtle

r = int(input("Please enter a radius of a circle: "))

t = turtle.Turtle()

f_c = ["blue", "black", "red"]
s_c = ["yellow", "green"]

t.speed(0)
t.pensize(2)

for i in range(3):
    t.pd()
    t.pencolor(f_c[i])
    t.circle(r)
    t.pu()
    t.fd((r * 2) + (r * 0.2))
    
t.goto(r, -r)

for i in range(2):
    t.pd()
    t.pencolor(s_c[i])
    t.circle(r)
    t.pu()
    t.fd((r * 2) + (r * 0.2))

turtle.done()
    