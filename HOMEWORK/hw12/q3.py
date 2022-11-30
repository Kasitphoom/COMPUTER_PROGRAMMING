import turtle
t = turtle

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(1)

class Rectangle2D():
    def __init__(self):
        self.minx = 0
        self.miny = 0
        self.maxx = 0
        self.maxy = 0
        

    def getRectangle(self,points):
        self.maxx = max([point.x for point in points])
        self.maxy = max([point.y for point in points])
        self.minx = min([point.x for point in points])
        self.miny = min([point.y for point in points])
        
        self.width = self.maxx - self.minx
        self.height = self.maxy - self.miny 

        self.midx = (self.width/2) + self.minx
        self.midy = (self.height/2) + self.miny

        t.penup()
        t.goto(self.minx,self.maxy)
        t.pendown()
        for i in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)
        
        print("Your rectangle center is at ({},{}) and it has the width of {} and height of {}".format(self.midx,self.midy,self.width,self.height))

pointinput = input("Enter the points : ")
listinput = pointinput.split(" ")
pointlist = []
for i in range(len(listinput)):
    if i > 0 and i % 2 == 1:
        temppoint = Point(float(listinput[i-1]),float(listinput[i]))
        pointlist.append(temppoint)

for i in pointlist:
    i.draw()

Rect = Rectangle2D()
Rect.getRectangle(pointlist)

t.done()