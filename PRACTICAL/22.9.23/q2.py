import turtle

x = int(input('Please enter size: '))

t = turtle.Turtle()

def square(x):
    i = 0
    while i < 4:
        t.fd(x)
        t.lt(90)
        i += 1
        
def draw(x):
    for i in range(4):
        for i in range(4):
            square(x * (i + 1))
        
        t.lt(90)
        
draw(x)
turtle.done()