text = ""
for i in range(5):
    i += 1
    text = ""
    for j in range(i):
        text += str(j + 1)
        
    print(text)
    
print("")
for i in range(5):
    print(text)
    text = text[:-1]
