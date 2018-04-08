
def get_prime(num):
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
	return (x)

primelist = [2,3]
for i in range(3,1000):
	primelist.append(get_prime(i))

i = 1
for x in primelist:
	xlen = len(str(x))
	while i <= xlen: