l1 = eval(input("Enter list1: "))
l2 = eval(input("Enter list2: "))

def get_the_difference(l1, l2):
    
    if len(l1) == 0 or len(l2) == 0:
        raise ValueError("List should not be empty")
    
    l3 = []
    for i in l1:
        if i not in l2:
            l3.append(i)
            
    for i in l2:
        if i not in l1:
            l3.append(i)
            
    return l3

print(get_the_difference(l1, l2))