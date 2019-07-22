n = int(input('Queens N : '))

stack = []
ans_count = 0

def check(col, row):
	global stack
	global ans_count
	# print(stack, col, row)
	for tmp_col in range(len(stack)):
		tmp_row = stack[tmp_col]
		if row == tmp_row:
			return
		elif abs(row - tmp_row) == (col - tmp_col):
			return
	if col == n - 1:
		ans_count += 1
		# print('Solution!')
		# print(stack)
	else:
		stack.append(row)
		for i in range(n):
			check(col+1, i)
		stack.pop()
		# print('pop')
		# print(stack, ans_count)
	return

for i in range(n):
	check(0, i)

print('Total Solution Counts : ' + str(ans_count))
