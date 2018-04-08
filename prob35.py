from prime_stuff import primes
import itertools
import timeit

start = timeit.default_timer()

# ---------------------------------------------- #
prime_set = set(n for n in primes(1000000))
circular_primes = 0

def check_circles(n):
	n = str(n)
	n0 = n
	for i in range(1, len(n)):
		exec('n'+str(i)+'=n'+str(i-1)+'[-1]+n'+str(i-1)+'[:-1]')
		if int(eval('n'+str(i))) not in prime_set:
			return False
	return True

for n in prime_set:
	if check_circles(n):
		circular_primes += 1

print(circular_primes)
# ---------------------------------------------- #

end = timeit.default_timer()
print('---> took', round(end - start, 3), 'seconds')