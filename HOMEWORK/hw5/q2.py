import turtle

fm = ["Month #1", "Month #2", "Month #3", "Month #4", "Month #5", "Month #6", "Month #7", "Month #8", "Month #9", "Month #10", "Month #11", "Month #12"]

week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

dstart = [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]
dend = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

turtle.setup()
turtle.screensize(2000, 2000)
turtle.tracer(0, 0)

t = turtle.Turtle()

w = 200

sw = w/7

t.speed(0)

def month(m):
    i = 0
    while i < 2:
        t.fd(w)
        t.lt(90)
        t.fd(sw)
        t.lt(90)
        i += 1
    
    t.pu()
    t.fd(w/2)
    t.pd()
    
    t.write("{} 2022".format(fm[m - 1]), font=('arial', 16, 'bold'), align='center')
    
    t.pu()
    t.bk(w/2)
    t.pd()


def Week():
    d = 0
    while d < 7:
        i = 0
        while i < 2:
            t.fd(sw/2)
            if i == 1:
                t.write(week[d], font=('arial', 8, 'bold'), align='center')
            t.fd(sw/2)
            t.rt(90)
            t.fd(sw)
            t.rt(90)
            i += 1
        
        t.fd(sw)
        d += 1
        
def date(m):
    x = 0
    d = 0
    i = 0
    while i < 5:
        
        t.pu()
        t.rt(90)
        t.fd(sw)
        t.lt(90)
        t.bk(w)
        t.pd() 
        j = 0
        while j < 7:
            b = 0
            while b < 2:
                t.fd(sw/2)
                if x >= dstart[m - 1] and d < dend[m - 1] and b == 1:
                    d += 1
                    t.write(str(d), font=('arial', 8, 'bold'), align='center')
                t.fd(sw/2)
                t.rt(90)
                t.fd(sw)
                t.rt(90)
                b += 1
            
            x += 1
          
            t.fd(sw)
            j += 1
        i += 1
            
def calendar_of_2022(m):
    month(m)
    Week()
    date(m)

t.pu()
t.goto(-900, 900)
t.pd()

i = 0
posx_init = -900
posy_init = 900
month_index = 0
while i < 3:
    t.pu()
    t.goto(posx_init, posy_init)
    t.pd()
    m = 0
    while m < 4:
        calendar_of_2022(month_index + 1)
        posy = t.ycor()
        posx = posx_init
        t.pu()
        t.goto(posx, posy - (sw * 3))
        t.pd()
        month_index += 1
        m += 1
    posx_init += w + 50
    i += 1

turtle.update()
turtle.hideturtle()
turtle.done()