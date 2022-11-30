phonebook = {}

while True:
    print("Phonebook Manager")
    print("Press '+' to add a new contact")
    print("Press '-' to delete a contact")
    print("Press 'f' to find a contact")
    print("Press 'p' to print all contacts")
    print("Press 'q' to quit")
    print("\n=====================================")
    choice = input("\nEnter your choice: ")
    
    if choice == "+":
        name = input("Enter name: ")
        number = input("Enter number: ")
        if number.isdigit():
            if name in phonebook.keys():
                print("\nContact already exists\n")
            else:
                phonebook[name] = number
                print(f"\n{name} has been added to the phonebook with number {number}\n")
        else:
            print("\nInvalid number\n")
    elif choice == "-":
        name = input("Enter name: ")
        if phonebook.keys().__contains__(name):
            print(f"\nPhone number of {name} ({phonebook[name]}) has been deleted\n")
            del phonebook[name]
        else:
            print(f"\n{name} is not in the phonebook\n")
    elif choice == "f":
        name = input("Enter name: ")
        if phonebook.keys().__contains__(name):
            print(f"\nPhone number of {name} is {phonebook[name]}\n")
        else:
            print(f"\n{name} is not in the phonebook\n")
    elif choice == "p":
        print()
        for name, number in phonebook.items():
            print(f"{name}: {number}")
            
        print()
    elif choice == "q":
        break
    else:
        print("\nXXXXXXXXX-----No command found-----XXXXXXXXX\n")
    
    print("=====================================")