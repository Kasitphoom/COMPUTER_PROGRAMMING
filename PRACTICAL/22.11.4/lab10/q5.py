l1 = eval(input("Enter list1: "))
l2 = eval(input("Enter list2: "))

def merge(l1, l2):
    l3 = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    while i < len(l1):
        l3.append(l1[i])
        i += 1
    while j < len(l2):
        l3.append(l2[j])
        j += 1
    return l3

print(merge(l1, l2))