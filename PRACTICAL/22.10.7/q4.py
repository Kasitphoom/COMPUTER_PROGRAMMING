class QuadraticEquation():
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getDiscriminant(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    
    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0
        
        return (-self.__b + (self.getDiscriminant() ** 0.5)) / (2 * self.__a)
    
    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        
        return (-self.__b - (self.getDiscriminant() ** 0.5)) / (2 * self.__a)
    
a = QuadraticEquation(1, -7, 12)
print(a.getRoot1())
print(a.getRoot2())