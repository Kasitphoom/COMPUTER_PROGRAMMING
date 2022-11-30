list1 = eval(input("Enter list: "))

def remove_the_thirds(list1):
    for i in range(len(list1)):
        if (i + 1) % 3 == 0:
            list1[i] = ""
    
    
    while "" in list1:
        list1.remove("")
        
remove_the_thirds(list1)

print(list1)