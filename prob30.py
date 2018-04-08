# Find the sum of all the numbers that can be written
# as the sum of fifth powers of their digits.

sum_powers = 0
terms = []

for i in range(1,1000000):
	for digit in str(i):
		sum_powers += int(digit) ** 5
	if i == sum_powers:
		terms.append(i)
		sum_powers = 0
	else:
		sum_powers = 0

print terms
print sum(terms[1:])