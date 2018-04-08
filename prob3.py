# What is the largest prime factor of the number 600851475143?
# The prime factors of 13195 are 5, 7, 13, and 29.

import numpy as np

primelist = range(1,7000,2)
primelist.append(2)
primelist.sort()

for x in range(1,7000,2):
	for y in np.arange(3,x,2):
		if x % y == 0:
			primelist.remove(x)
			break

print primelist

number = 600851475143
factorlist = []

for x in primelist:
	if number % x == 0:
		factorlist.append(x)
		number /= x

print factorlist