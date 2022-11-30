class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
        
    def printInfo(self):
        print(f"Position: {self.x}, {self.y}")
        
class Circle(Point):
    def __init__(self, x = 0.0, y = 0.0, r = 0.0):
        super().__init__(x, y)
        self.r = r
        
    def area(self):
        return 3.14 * self.r * self.r
        
    def printInfo(self):
        print(f"Position: {self.x}, {self.y}, Radius: {self.r}, Area: {self.area()}")
        
p = Point(10,20)
p.printInfo()

c = Circle(10,20,5)
print(c.area())
c.printInfo()
