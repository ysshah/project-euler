# There exists one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

pythag = []
limit = 100
test_range = range(1,limit)

# Define greatest common divisor function
def gcd(a, b):
	# Return greatest common divisor using Euclid's Algorithm.
	while b:
		a, b = b, a % b
	return a

# For every number in test_range (given a < b < c)
# If a^2 + b^2 = c^2 and if the GCD is 1, append triplet to pythag
for a in test_range:
	for b in range(a,limit):
		for c in range(b,limit):
			if c**2 == a**2 + b**2:
				if gcd(a,gcd(b,c)) == 1:
					pythag.append([a, b, c])

# For every triplet in pythag, multiply by range, check to see if it is = 1000
for f in pythag:
	for mult in range(1,limit):
		if sum(k*mult for k in f) == 1000:
			print([k*mult for k in f])
			answer = 1
			for i in [k*mult for k in f]:
				answer *= i
			print(answer)
			break