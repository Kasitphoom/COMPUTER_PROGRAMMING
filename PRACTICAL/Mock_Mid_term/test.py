import turtle
t = turtle.Turtle()

def draw_hex(n):
    for i in range(6):
        t.fd(n)
        t.lt(360/6)
    
def squirl_hex(s):
    n = s
    half = 0
    while n > 10:
        half = n/2
        t.pu()
        t.bk(half)
        t.rt(90)
        t.fd(n)
        t.lt(90)
        t.pd()
        draw_hex(n)
        t.pu()
        t.lt(90)
        t.fd(n)
        t.rt(90)
        t.fd(half)
        t.lt(30)
        
        n *= 0.75

squirl_hex(80)
turtle.done()