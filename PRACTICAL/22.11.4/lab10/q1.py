def name_list():
    arr = []
    while True:
        name = input("Enter name: ")
        if len(name) == 0:
            break
        
        arr.append(name)
    return arr


print(name_list())