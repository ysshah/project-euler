from prime_stuff import primes
import timeit

start = timeit.default_timer()

# ---------------------------------------------- #
check_till = 100000

prime_set = set(primes(check_till))
composites = []
for i in range(9,check_till+1,2):
	if i not in prime_set:
		composites.append(i)

twice_squares = set([2*(i**2) for i in range(1,100)])

def checker(x):
	for p in prime_set:
		for ts in twice_squares:
			if x == p + ts:
				# print(x, '=', p, '+', ts)
				return True
	return False

i = 0
while checker(composites[i]):
	i += 1

print('answer =', composites[i])
# ---------------------------------------------- #

end = timeit.default_timer()
print('---> took', round(end - start, 3), 'seconds')