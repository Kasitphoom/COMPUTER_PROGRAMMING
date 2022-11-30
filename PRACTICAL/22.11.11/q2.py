class Calculator:
    def __init__(self, acc = 0.0):
        self.acc = acc
    
    def set_accumulator(self, a):
        self.acc = a
        
    def get_accumulator(self):
        return self.acc
    
    def add(self, x):
        self.acc += x
    
    def subtract(self, x):
        self.acc -= x
    
    def multiply(self, x):
        self.acc *= x
    
    def divide(self, x):
        if x == 0:
            return
        
        self.acc /= x
    
    def print_result(self):
        print(f"Result: {self.acc}")
        
class Sci_calc(Calculator):
    def __init__(self, acc = 0.0):
        super().__init__(acc)
        
    def square(self):
        self.acc *= self.acc
    
    def exp(self, x):
        self.acc **= x
        
    def factorial(self):
        n = 1
        for i in range(1, int(self.acc) + 1):
            n *= i
        self.acc = n
    
    def print_result(self):
        print(f"Result: {self.acc:e}")
        
cal = Calculator()

cal.set_accumulator(100)
cal.print_result()

cal.add(20)

cal.subtract(10)
cal.print_result()

cal.multiply(2)

cal.divide(5)
print(cal.get_accumulator())

try:
    cal.divide(0)
except:
    print("this line should not be printed")

sci = Sci_calc()

sci.set_accumulator(100)
sci.square()
sci.print_result()

sci.set_accumulator(4)
sci.exp(3)
print(sci.get_accumulator())

sci.set_accumulator(5)
sci.factorial()
sci.print_result()
        