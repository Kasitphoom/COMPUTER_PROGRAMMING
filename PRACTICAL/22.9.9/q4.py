sum = 0
last_n = 0
for i in range(5):
    n = int(input("Enter an interger: "))
    
    if (n * last_n) < 0:
        sum = 0
        
    sum += n
    last_n = n
    
    print("Current sum:\t", sum)
    