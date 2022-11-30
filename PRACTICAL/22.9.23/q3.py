def draw_polygon(x, y, side = 4, size = 100):
    import turtle
    t = turtle.Turtle()
    t.pu()
    t.goto(x, y)
    t.pd()
    for i in range(side):
        t.fd(size)
        t.lt(360/side)
    turtle.done()
    
eval(input("Enter function to draw polygon: "))