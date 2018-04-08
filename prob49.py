import itertools
from prime_stuff import primes
import timeit

start = timeit.default_timer()

# ---------------------------------------------- #
prime_nums = set(primes(10000)[168:])
checklist = list(range(1000,9999))

def find():
	for n in checklist:
		perms = list(itertools.permutations([i for i in str(n)]))
		combs = list(itertools.combinations(perms,3))
		for c in combs:
			a = int(''.join(c[0]))
			b = int(''.join(c[1]))
			c = int(''.join(c[2]))
			if a < b < c and c - b == b - a:
				if a in prime_nums and b in prime_nums and c in prime_nums:
					if a != 1487:
						return a, b, c

ans = find()

print('numbers =', str(ans)[1:-1])
print('answer =', ''.join(str(n) for n in ans))
# ---------------------------------------------- #

end = timeit.default_timer()
print('---> took', round(end - start, 3), 'seconds')