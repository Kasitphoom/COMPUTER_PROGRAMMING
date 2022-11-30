score = int(input("Please enter your score: "))

if score not in range(0,100):
    print("Invalid score")
    exit()

if score >= 80:
    g = "A"
elif score >= 70:
    g = "B"
elif score >= 60:
    g = "C"
elif score >= 50:
    g = "D"
else:
    g = "F"
    
print("Your grade is: ", g)