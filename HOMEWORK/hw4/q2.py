xy1 = input("Enter the center point of rectangle 1: ")
width1 = int(input("Enter the width of rectangle 1: "))
height1 = int(input("Enter the height of rectangle 1: "))

xy2 = input("Enter the center point of rectangle 2: ")
width2 = int(input("Enter the width of rectangle 2: "))
height2 = int(input("Enter the height of rectangle 2: "))

xy1 = xy1.replace(" ","").split(",")
xy2 = xy2.replace(" ","").split(",")

for i in range(len(xy1)):
    xy1[i] = float(xy1[i])
for i in range(len(xy2)):
    xy2[i] = float(xy2[i])
    
lt1 = [xy1[0] - width1/2, xy1[1] + height1/2]
rb1 = [xy1[0] + width1/2, xy1[1] - height1/2]

lt2 = [xy2[0] - width2/2, xy2[1] + height2/2]
rb2 = [xy2[0] + width2/2, xy2[1] - height2/2]

area1 = width1 * height1
area2 = width2 * height2

def checkOverlap(lt1, rb1, lt2, rb2):
    if (lt1[0] > rb2[0]) or (rb1[0] < lt2[0]) or (lt1[1] < rb2[1]) or (rb1[1] > lt2[1]):
        return False
    else:
        return True
    
print("\nResult:")
  
if area1 > area2 and lt1[0] < lt2[0] and (lt1[0] + width1) > (lt2[0] + width2) and rb1[1] < rb2[1] and (rb1[1] + height1) > (rb2[1] + height2):
    print("Rectange 2 is inside Rectangle 1")
elif area2 > area1 and lt2[0] < lt1[0] and (lt2[0] + width2) > (lt1[0] + width1) and rb2[1] < rb1[1] and (rb2[1] + height2) > (rb1[1] + height1):
    print("Rectange 1 is inside Rectangle 2")
else:
    if checkOverlap(lt1, rb1, lt2, rb2):
        print("The two rectangles overlap")