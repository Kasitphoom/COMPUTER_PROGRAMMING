import turtle

p1 = input("Please enter first point: ")
p2 = input("Please enter second point: ")
p3 = input("Please enter third point: ")

p1 = p1.replace(" ", "").replace("(", "").replace(")", "").split(",")
p2 = p2.replace(" ", "").replace("(", "").replace(")", "").split(",")
p3 = p3.replace(" ", "").replace("(", "").replace(")", "").split(",")

h = [int(p1[1]), int(p2[1]), int(p3[1])]

h.sort()

print(h)

def length(p1, p2):
    return ((int(p1[0]) - int(p2[0])) ** 2 + (int(p1[1]) - int(p2[1])) ** 2) ** 0.5

l1 = length(p1, p2)
l2 = length(p2, p3)
l3 = length(p3, p1)

def area(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    return (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5

t = turtle.Turtle()

t.pu()
t.goto(int(p1[0]), int(p1[1]))
t.pd()
t.goto(int(p2[0]), int(p2[1]))
t.goto(int(p3[0]), int(p3[1]))
t.goto(int(p1[0]), int(p1[1]))

t.pu()

pos = t.position()[0]

t.goto(pos, h[0] - 20)

t.pd()
t.write(f"Area: {area(l1, l2, l3):.2f}")

turtle.done()