for i in range(50, 0, -1):

	if i % 3 == 0 or i % 5 == 0:
		continue
	
	print(i, end=",")