class Poly:
    def __init__(self, x):
        self.x = x
        
    def add(self, p):
        temp = []
        for i in range(len(p.x)):
            temp = list(p.x)
            temp[i] += self.x[i]
            p.x = tuple(temp)
        
        return p.x
    
    def scalar_multiply(self, n):
        temp = []
        for i in range(len(self.x)):
            temp = list(self.x)
            temp[i] *= n
            self.x = tuple(temp)
            
        return self.x
    
    def multiply(self, p):
        result = [0] * (len(self.x) + len(p.x) - 1)
        for i in range(len(self.x)):
            for j in range(len(p.x)):
                result[i + j] += self.x[i] * p.x[j]
                
        return tuple(result)
    
    def power(self, n):
        result = [1]
        for i in range(n):
            result = self.multiply(Poly(result))
            
        return Poly(result)
    
    def diff(self):
        result = [0] * (len(self.x) - 1)
        for i in range(1, len(self.x)):
            result[i - 1] = self.x[i] * i
            
        return Poly(tuple(result))
    
    def intergrate(self):
        result = [0] * (len(self.x) + 1)
        for i in range(len(self.x)):
            result[i + 1] = self.x[i] / (i + 1)
            
        return Poly(tuple(result))
    
    def eval(self, n):
        result = 0
        for i in range(len(self.x)):
            result += self.x[i] * n ** i
            
        return result

    def print(self):
        for i in range(len(self.x)):
            
            if i != 0 and self.x[i] > 0:
                print("+", end=" ")
            
            print(f"{self.x[i]}", end="")
            if i == 0:
                print(" ", end="")
                continue
            
            print(f"x^{i}", end=" ")
            
        print()

p = Poly((1, 2, 3 ,4))

p2 = Poly((1,2,3))

p.add(p2).print()