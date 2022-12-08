def count_operands_in_expr(tuple_in):
	
	if type(tuple_in) != tuple:
		return 1
	else:
		return count_operands_in_expr(tuple_in[0]) + count_operands_in_expr(tuple_in[2])

print(count_operands_in_expr((3,'**',4)))
print(count_operands_in_expr(((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4))))