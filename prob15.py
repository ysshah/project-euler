def counter(nright, ndown, maxright, maxdown):
	memo_table = {}
	def counter(nright, ndown, maxright, maxdown):
		if (nright, ndown, maxright, maxdown) not in memo_table:
			memo_table[nright, ndown, maxright, maxdown] = full_counter(nright, ndown, maxright, maxdown)
		return memo_table[nright, ndown, maxright, maxdown]
	def full_counter(nright, ndown, maxright, maxdown):
		if nright > maxright or ndown > maxdown:
			return 0
		if nright == maxright and ndown == maxdown:
			return 1
		if nright == maxright:
			return counter(nright, ndown + 1, maxright, maxdown)
		if ndown == maxdown:
			return counter(nright + 1, ndown, maxright, maxdown)
		else:
			return counter(nright + 1, ndown, maxright, maxdown) + counter(nright, ndown + 1, maxright, maxdown)
	return counter(nright, ndown, maxright, maxdown)

print('answer =', counter(0,0,20,20))