f = input("Enter firstname: ")
l = input("Enter lastname: ")
g = input("Enter Gender: ")

if g != "M" and g != "F":
    raise Exception("Gender must be M or F")

username = g + l[0] + f[:6]
print(username.upper())