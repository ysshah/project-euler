# Original
def count_change1(amount, denoms = (50, 25, 10, 5, 1)):
	"""Original"""
	if amount == 0:
		return 1
	elif len(denoms) == 0:
		return 0
	elif amount >= denoms[0]:
		return count_change1(amount - denoms[0], denoms) + count_change1(amount, denoms[1:])
	else:
		return count_change1(amount, denoms[1:])

# Memoization
def count_change(amount, denoms = (50, 25, 10, 5, 1)):
	"""Memoization"""
	memo_table = {}
	def count_change(amount, denoms):
		if (amount, denoms) not in memo_table:
			memo_table[amount, denoms] = full_count_change(amount, denoms)
		return memo_table[amount, denoms]
	def full_count_change(amount, denoms):
		if amount == 0:
			return 1
		elif len(denoms) == 0:
			return 0
		elif amount >= denoms[0]:
			return count_change(amount - denoms[0], denoms) + count_change(amount, denoms[1:])
		else:
			return count_change(amount, denoms[1:])
	return count_change(amount, denoms)

# Faster Memoization
def count_change(amount, denoms = (50, 25, 10, 5, 1)):
	"""Faster Memoization"""
	memo_table = [ [-1] * (len(denoms)+1) for i in range(amount+1) ]
	def count_change(amount, denoms):
		if memo_table[amount][len(denoms)] == -1:
			memo_table[amount][len(denoms)] = full_count_change(amount, denoms)
		return memo_table[amount][len(denoms)]
	def full_count_change(amount, denoms):
		if amount == 0:
			return 1
		elif len(denoms) == 0:
			return 0
		elif amount >= denoms[0]:
			return count_change(amount - denoms[0], denoms) + count_change(amount, denoms[1:])
		else:
			return count_change(amount, denoms[1:])
	return count_change(amount, denoms)

print(count_change(200, (200, 100, 50, 20, 10, 5, 2, 1)))