def inttobinary(n):
    if n == 0:
        return "0"
    elif n < 0:
        return "Error: Input is negative"
    else:
        bi = n % 2
        leftover = n // 2
        if leftover == 0:
            return str(bi)
        else:
            return inttobinary(leftover) + str(bi)
        
def binarytoint(s):
    sum = 0
    for i in range(len(s), 0, -1):
        if s[i-1] == "1":
            sum += 2**(len(s)-i)
    
    return sum

n = input("Enter a positive integer: ")

print(inttobinary(int(n)))
print(binarytoint(inttobinary(int(n))))