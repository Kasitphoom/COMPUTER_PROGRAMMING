import turtle

class Rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
        
    def intersect(self, rec):
        if self.x + self.width < rec.x or self.y - self.height > rec.y:
            return Rectangle(0,0,0,0)
        else:
            selfx2 = self.x + self.width
            selfy2 = self.y - self.height
            rec_newx = rec.x + rec.width
            rec_newy = rec.y - rec.height
            
            newx = max(self.x, rec.x)
            newy = min(self.y, rec.y)
            
            newwidth = min(selfx2, rec_newx) - newx
            newheight = newy - max(selfy2, rec_newy)
            
            return Rectangle(newx, newy, newwidth, newheight)
            
    
    def draw(self):
        import turtle
        t = turtle.Turtle()
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)
        
class Circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def getArea(self):
        return 3.14 * self.radius ** 2
    
    def getPerimeter(self):
        return 2 * 3.14 * self.radius
    
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    
    def draw(self):
        t = turtle.Turtle()
        t.pu()
        t.goto(self.x, self.y - self.radius)
        t.pd()
        t.circle(self.radius)
        turtle.done()


a = Rectangle(0, 0, 100, 100)
b = Rectangle(300, 50, 100, 200)

print(a.getArea())
print(b.getPerimeter())

c = a.intersect(b)

a.draw()
b.draw()
c.draw()

c.move(-100, -100)

c.draw()

circle = Circle(-100, 0, 100)
circle.draw()