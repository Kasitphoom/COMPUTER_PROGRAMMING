p0 = input("Enter the first point: ")
p1 = input("Enter the second point: ")
p2 = input("Enter the third point: ")

p0 = p0.split(',')
p1 = p1.split(',')
p2 = p2.split(',')

for i in range(len(p0)):
    p0[i] = float(p0[i])
for i in range(len(p1)):
    p1[i] = float(p1[i])
for i in range(len(p2)):
    p2[i] = float(p2[i])

midPoint = [(p0[0] + p1[0])/2, (p0[1] + p1[1])/2]

if p2[0] < midPoint[0]:
    print("The point is on the left side of the line")
else:
    print("The point is on the right side of the line")
    
gradient_ref = (p1[1] - p0[1])/(p1[0] - p0[0])

gradient_check = (p2[1] - midPoint[1])/(p2[0] - midPoint[0])

if (gradient_ref == gradient_check) and (int(p2[0]) in range(int(p0[0]), int(p1[0]))):
    print("The point is on the line")
else:
    print("The point is not on the line")