money = int(input("Enter the amount of money: "))

thousand = money // 1000
leftover = money % 1000

f_hundred = leftover // 500
leftover = leftover % 500

o_hundred = leftover // 100
leftover = leftover % 100

fifty = leftover // 50
leftover = leftover % 50

twenty = leftover // 20
leftover = leftover % 20

two = leftover // 2
leftover = leftover % 2

one = leftover

if thousand > 0:
    print("1000-baht notes: " + str(thousand))

if f_hundred > 0:
    print("500-baht notes: " + str(f_hundred))

if o_hundred > 0:
    print("100-baht notes: " + str(o_hundred))

if fifty > 0:
    print("50-baht notes: " + str(fifty))
    
if twenty > 0:
    print("20-baht notes: " + str(twenty))

if two > 0:
    print("2-baht coins: " + str(two))
    
if one > 0:
    print("1-baht coins: " + str(one))