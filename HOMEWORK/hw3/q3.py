import turtle

l = int(input("Please enter a length of a star: "))

t = turtle.Turtle()

t.lt(34)

for i in range(5): 
    t.fd(l)
    t.lt(144)
    
turtle.done()