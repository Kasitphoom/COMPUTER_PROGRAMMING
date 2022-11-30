n = int(input("Enter a number (1 or more than): "))

if n < 1:
    raise Exception("Number must be 1 or more than 1")

base = n
half = (n // 2) + 1
s_half = n - half
while n > 0:
    temp = n
    n -= 1
    for i in range(n):
        print("*" * (i + 1))
    
    while temp > 0:
        print("*" * temp)
        if temp <= 2:
            temp -= 2
        else:
            temp -= 1
            
if base != 1:
    print("*")