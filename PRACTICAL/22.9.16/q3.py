import turtle

n = int(input("Enter the number of square: "))

small_n = 100/n

t = turtle.Turtle()

t.speed(0)

c = ['grey', 'white']
x = 0

for i in range(n):
    
    for i in range(n):
        t.fillcolor(c[x % 2])
        t.begin_fill()
        for i in range(4):
            t.fd(small_n)
            t.rt(90)
        t.end_fill()
        t.pu()
        t.fd(small_n)
        t.pd()
        x += 1
    
    if n % 2 == 0:
        x += 1
        
    t.pu()
    t.bk(100)
    t.rt(90)
    t.fd(small_n)
    t.lt(90)
    t.pd()
    
turtle.done()