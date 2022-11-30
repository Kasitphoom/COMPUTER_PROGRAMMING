import turtle

n = int(input("Enter the number of square: "))

small_n = 100/n

t = turtle.Turtle()

t.speed(0)

for i in range(n):
    for i in range(n):
        for i in range(4):
            t.fd(small_n)
            t.rt(90)
        t.pu()
        t.fd(small_n)
        t.pd()
    t.pu()
    t.bk(100)
    t.rt(90)
    t.fd(small_n)
    t.lt(90)
    t.pd()
    
turtle.done()