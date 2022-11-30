short = input("Enter a short word: ")
long = input("Enter a long word: ")

start = 0
end = 0
found = False
while start < len(long):
    
    if long[start] == short[end]:
        end += 1
        if end == len(short):
            found = True
            break
    
    start += 1
        
if found:
    print(True)
else:
    print(False)