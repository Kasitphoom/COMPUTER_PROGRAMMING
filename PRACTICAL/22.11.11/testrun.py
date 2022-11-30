import q1 as test1

p = test1.Point(10,20)
p.printInfo()

c = test1.Circle(10,20,5)
print(c.area())
p.printInfo()

import q2 as test2

cal = test2.Calculator()

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

sci = test2.Sci_calc()

sci.set_accumulator(100)
sci.square()
sci.print_result()

sci.set_accumulator(4)
sci.exp(3)
print(sci.get_accumulator())

sci.set_accumulator(5)
sci.factorial()
sci.print_result()


import q4 as test4
import q5 as test5

try:
    trap = test4.TwoDShape(0,0)
    trap.draw()
except:
    print("This line should be printed")
    

shape = []

l1 = test4.Line((0.5, 0.6), (4.8, 9.0))
shape.append(l1)
r1 = test4.Rectangle((10, 30), (200, 150))
shape.append(r1)
c1 = test4.Circle(0.5, 0.6, 300)
shape.append(c1)
r2 = test4.Rectangle((-50, 80), (300, 400))
shape.append(r2)
c2 = test4.Circle(-20, -30, 100)
shape.append(c2)

s1 = test5.Square(0, 0, 100)
shape.append(s1)


for s in shape:
    s.draw()

  

import q6 as test6

try:
    trap = test6.Transportation("", "", 0.0)
    print(trap.find_cost())
except:
    print("This line should be printed")
    


walk = test6.Walk("KMITL", "KMITL SCB Bank", 0.6)
taxi = test6.Taxi("KMITL SCB Bank", "Ladkrabang Station", 5)
train = test6.Train("Ladkrabang Station", "Payathai Station", 40, 6)
taxi2 = test6.Taxi("Payathai Station", "The British Council", 3)
John = [walk, taxi, train, taxi2]
for travel in John:
  print(travel.find_cost())