import turtle

fm = ["January","February","March","April","May","June","July","August","September","October","November","December"]

week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

dstart = [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]
dend = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

t = turtle.Turtle()

w = 200

sw = w/7

t.speed(0)

def month(m):
    for i in range (2):
        t.fd(w)
        t.lt(90)
        t.fd(sw)
        t.lt(90)
    
    t.pu()
    t.fd(w/2)
    t.pd()
    
    t.write("{} 2022".format(fm[m - 1]), font=('arial', 16, 'bold'), align='center')
    
    t.pu()
    t.bk(w/2)
    t.pd()

def Week():
    for d in range(7):
        for i in range(2):
            t.fd(sw/2)
            if i == 1:
                t.write(week[d], font=('arial', 8, 'bold'), align='center')
            t.fd(sw/2)
            t.rt(90)
            t.fd(sw)
            t.rt(90)
        
          
        t.fd(sw)
        
def date(m):
    x = 0
    d = 0
    for i in range(5):
        
        t.pu()
        t.rt(90)
        t.fd(sw)
        t.lt(90)
        t.bk(w)
        t.pd()
        for i in range(7):
            for i in range(2):
                t.fd(sw/2)
                if x >= dstart[m - 1] and d < dend[m - 1] and i == 1:
                    d += 1
                    t.write(str(d), font=('arial', 8, 'bold'), align='center')
                t.fd(sw/2)
                t.rt(90)
                t.fd(sw)
                t.rt(90)
            
            x += 1
          
            t.fd(sw)
        
    
    
    

def calendar_of_2022(m):
    month(m)
    Week()
    date(m)
    

eval(input())
turtle.done()