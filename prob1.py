# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np

# ------------- Method 1 -------------- #
# Calculate multiples of 3 & 5 up till 1000, merge lists and take out repeats

k_threes = np.arange(1,334)
k_fives = np.arange(1,200)

threes = []
fives = []

for x in k_threes:
	threes.append(3*x)
for x in k_fives:
	fives.append(5*x)

both = np.unique(threes + fives)

print sum(both)

# ------------- Method 2 -------------- #
# Brute force: Check if [1, 2, 3...1000] is divisible by 3 or 5

sumMult = 0
for x in np.arange(1,1000):
	if x % 3 == 0 or x % 5 == 0:
		sumMult += x

print sumMult