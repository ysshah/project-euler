def get_prime(num):
	""" Get the num_th prime number """
	i = 3
	n = 1
	s = 1

	while (i <= num):
		if (s == 1):
			x = 6 * n - 1
			s = 0
		else:
			x = 6 * n + 1
			s = 1
			n = n + 1
		r = x ** 0.5
		p = 1
		t = 3
		while (t <= r):
			if(x % t == 0):
				p = 0
			t = t + 2
		if (p == 1):
			i = i + 1
	print (x)

def primes(n):
	""" Returns a list of prime numbers from 2 to < n """
	if n < 2:
		return []
	if n == 2:
		return [2]
	# do only odd numbers starting at 3
	s = list(range(3, n, 2))
	# n**0.5 may be slightly faster than math.sqrt(n)
	mroot = n ** 0.5
	half = len(s)
	i = 0
	m = 3
	while m <= mroot:
		if s[i]:
			j = (m * m - 3)//2
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i + 1
		m = 2 * i + 3
	# make exception for 2
	return [2]+[x for x in s if x]