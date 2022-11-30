c = ""
uni = ""
type = ""
while True:
	c = input("Please enter a character: ")
	
	uni = hex(ord(c))
	if uni >= "0x30" and uni <= "0x39":
		type = "Numberic Charater"
	elif uni >= "0x41" and uni <= "0x5a":
		type = "Capital Letter"
	elif uni >= "0x61" and uni <= "0x7a":
		type = "Small-case Letter"
	elif uni == "0x2e":
		print("Good bye.")
		break
	else:
		type = "Special Character"
	
	print(f"It's a {type}")
	print(int("0x61", base=0))