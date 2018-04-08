# Find the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20

test = 2520.
numlist = range(3,21)
idx = 0

while idx <= len(numlist)-1:
	if test % numlist[idx] != 0:
		test += 20
		idx = 0
	else:
		idx += 1
		if idx == len(numlist):
			print test