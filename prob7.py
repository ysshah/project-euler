# What is the 10001st prime number? (Starting with 2, 3, 5, 7, 11, 13...)

def prime_num(n):
	primelist = [2,3]
	k = 1
	test_term = 5
	while len(primelist) < n:
		for y in range(1,len(primelist)):
			if test_term % primelist[y] != 0:
				k += 1
				if k == len(primelist):
					primelist.append(test_term)
					test_term += 2
					k = 0
					break
			else:
				k = 0
				test_term += 2
	return primelist[n - 1]

print(prime_num(10001))