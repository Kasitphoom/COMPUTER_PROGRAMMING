n = int(input("Enter the number of lines: "))
val = 0
last_val = ""
if n % 2 == 0:
    l = int(n / 2)
    
    last_int_val = 1
    for i in range(l):
        last_val = str(last_int_val) + last_val
        val = last_int_val * 2
        last_int_val = val
        print(last_val)
    
    t_val = ""
    for i in range(l):
        t_val = last_val[1:]
        last_val = t_val
        print(t_val)
else:
    l = (n // 2) + 1
    
    last_int_val = 1
    for i in range(l):
        last_val = str(last_int_val) + last_val
        val = last_int_val * 2
        last_int_val = val
        print(last_val)
    
    t_val = ""
    for i in range(l-1):
        t_val = last_val[1:]
        last_val = t_val
        print(t_val)