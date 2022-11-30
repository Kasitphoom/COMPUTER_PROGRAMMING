name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
weight = input("Please enter your weight (kg): ")
height = input("Please enter your height (cm): ")

bmi = float(weight) / ((float(height) / 100) ** 2)

if age < 18:
    if bmi < 15:
        res = "underweight"
    elif bmi <= 20:
        res = "normal"
    else:
        res = "overweight"
elif age <= 35:
    if bmi < 18:
        res = "underweight"
    elif bmi <= 24:
        res = "normal"
    else:
        res = "overweight"
else:
    if bmi < 19:
        res = "underweight"
    elif bmi <= 26:
        res = "normal"
    else:
        res = "overweight"
        
print(f"Your body mas index is {bmi:.9f}\n{name}, you are {res}.")