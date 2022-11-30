val = 0
t = ""
i = 0
while i < 49:
    i += 1
    if i % 3 == 0:
        continue
    
    t += (str(i) + ", ")

print(t)