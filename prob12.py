tri_num = 1
i = 2
divisors = []
factors = []
import timeit

def f(val):
    factors = []
    for i in range(1, int(val**0.5)+1):
        if val % i == 0:
            factors.extend([i, int(val / i)])
    return factors

start = timeit.default_timer()
while len(factors) < 500:
	factors = []

	tri_num += i
	factors = f(tri_num)

	# print(len(factors))
	i += 1
stop = timeit.default_timer()

print('The triangle number is %i. It has %i factors.' %(tri_num, len(factors)))
print('Took %2.3f seconds' %(stop-start))