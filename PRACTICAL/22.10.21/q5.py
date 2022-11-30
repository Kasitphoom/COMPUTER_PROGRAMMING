def LCS(s1, s2):
    
    final = [s1[i:b+1] for i in range(len(s1)) for b in range(len(s1))]
    asub = [i for i in final if i in s1 and i in s2 and len(i) > 1]
    
    if len(asub) == 0:
        return ""

    return max(asub, key=len)
s1 = input("Enter a string: ")
s2 = input("Enter a string: ")

print(LCS(s1, s2))