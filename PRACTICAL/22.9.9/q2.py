n = input("Please enter the number: ")

print(type(n))
   


try:
    val = int(n)
    c_int = True
except ValueError:
    try:
        val = float(n)
        c_int = False
    except ValueError:
        print("Not a number")
        exit()

if c_int:
    print("number is integer.\nWhich format do you want to print?\n1. Binary\n2. Octal\n3. Hexadecimal\n4. Decimal")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(format(val,"b"))
    elif choice == "2":
        print(format(val,"o"))
    elif choice == "3":
        print(format(val,"x"))
    elif choice == "4":
        print(format(val,".1f"))
elif not c_int:
    print("number is not an interger.\nWhich format do you want to print?\n1. floating point\n2. scientific format")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(format(val,"f"))
    elif choice == "2":
        print(format(val,"e"))
    

        