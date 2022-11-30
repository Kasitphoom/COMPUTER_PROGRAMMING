class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
        
    def isSolvable(self):
        return self.__a * self.__d - self.__b * self.__c != 0
    
    def getX(self):
        res = ((self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)) if self.isSolvable() else None
        return res
    
    def getY(self):
        res = ((self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)) if self.isSolvable() else None
        return res
    
linear = LinearEquation(9, 4, 3, -5, -6, -21)
print(linear.getA())
print(linear.getB())
print(linear.getC())
print(linear.getD())
print(linear.getE())
print(linear.getF())
print(linear.isSolvable())
print(linear.getX())
print(linear.getY())
