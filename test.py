sum_nums = 0

def recursion(num):
	if num == 0:
		return 0
	else:
		return num + recursion(num-1)
		