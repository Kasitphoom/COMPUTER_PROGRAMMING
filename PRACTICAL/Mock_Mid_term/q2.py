money = int(input("How Much you want to withdraw: "))

thousand = money // 1000
left_over = money % 1000

f_hundred = left_over // 500
left_over = left_over % 500

o_hundred = left_over // 100

print("You get: ", end = ' ')

if thousand > 0:
	print(f"\t{thousand} notes of 1,000 Bahts")

if f_hundred > 0:
	print(f"\t{f_hundred} notes of 500 Bahts")

if o_hundred > 0:
	print(f"\t{o_hundred} notes of 100 Bahts")