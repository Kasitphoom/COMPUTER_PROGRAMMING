n = input("Enter grade of students: ")

def check_grades(g):
    if g > 100 or g < 0:
        raise ValueError("Grade must be less than 100 and more than 0")
    elif g>= 80:
        return "A"
    elif g>= 70:
        return "B"
    elif g>= 60:
        return "C"
    elif g>= 50:
        return "D"
    else:
        return "F"
    
try:
    val = int(n)
    c_int = True
except ValueError:
    try:
        val = float(n)
        c_int = True
    except ValueError:
        raise ValueError("Value has to be a number")
    
if c_int:
    print(check_grades(val))

