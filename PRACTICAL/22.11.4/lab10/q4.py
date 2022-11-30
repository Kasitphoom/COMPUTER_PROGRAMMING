import turtle
s = eval(input("Enter list: "))

def countfreq(s):
    s.sort()
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

def histogram(s):
    freq = countfreq(s)
    max_char = max(freq, key=freq.get)

    t = turtle.Turtle()

    t.lt(90)
    t.fd(freq[max_char]*20)
    t.write("Y")
    t.pu()
    t.goto(0,0)
    t.rt(90)
    t.pd()
    t.fd(10)
    for i in freq:
        
        c_x = t.xcor()
        t.pu()
        t.goto(c_x, -25)
        t.pd()
        t.write(i, font=("Arial", 12, "normal"))
        t.pu()
        t.goto(c_x, 0)
        t.pd()
        t.lt(90)
        for j in range(2):
            t.fd(freq[i]*20)
            t.rt(90)
            t.fd(20)
            t.rt(90)
        t.rt(90)
        t.fd(20)
    
    t.fd(10) 
    t.write("X")
    turtle.done()

histogram(s)