# Which starting number, under one million, produces the longest Collatz
# sequence? [defined by n --> n/2 (n is even) and n --> 3n + 1 (n is odd)]

length = []

for num in range(1,1000000):
	sequence = [num]
	while num > 1:
		if num % 2 == 0:
			num /= 2
			sequence.append(num)
		else:
			num = 3*num + 1
			sequence.append(num)
	length.append(len(sequence))

print length.index(max(length))+1