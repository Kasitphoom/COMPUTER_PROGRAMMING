import turtle
import random


t = turtle.Turtle()
# setting radius
rad = 200

def pie_chart(arr):
    
    # get how many numbers are in the array
    totalNo = len(arr)
    
    # count for duplicate values
    cres = arr_count(arr)
    
    # get proportional values (percentage)
    prop = {}
    for key,val in cres.items():
        prop[key] = val/totalNo
    
    print(prop)
    
    # draw the graph
    prev_h = 0
    for i in prop:
        t.pd()
        
        # get current heading for the pen
        ch = 360 * prop[i]
        
        # random hedxadecimal number for color
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        
        print(f"Current Heading: {ch} // Previous Heading: {prev_h}")
        
        # set fill color
        t.fillcolor(hexadecimal[0])
        t.begin_fill()
        
        # draw circle by the percentage
        t.fd(rad)
        t.lt(90)
        t.circle(rad, ch)
        
        # reset the position of the pen
        t.pu()
        t.setpos(0,0)
        
        # set pen heading to new heading using last heading value
        t.setheading(prev_h + ch)
        t.pd()
        
        # draw a line to last position
        t.fd(rad)
        
        # set pen heading to new heading using last heading value
        t.pu()
        t.setpos(0,0)
        t.setheading(prev_h + ch)
        t.end_fill()
        
        # store last position adding with current position to use in next loop
        prev_h = prev_h + ch

    
    
def arr_count(arr):
    res = {}
    for i in arr:
        res[i] = arr.count(i)
        
    return res

exec(input())
turtle.done()

"""
example:
pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3])
"""