# Find the sum of all products whose multiplicand/multiplier/product 
# identity can be written as a 1 through 9 pandigital.

import itertools
import numpy as np

p = itertools.permutations([1,2,3,4,5,6,7,8,9])
all_p = list(p)
pandigitals = []

# 1 digit * 4 digits = 4 digits
for num in all_p:
	multiplicand = int(str(num[0]).strip('()').replace(', ',''))
	multiplier = int(str(num[1:5]).strip('()').replace(', ',''))
	product = int(str(num[5:10]).strip('()').replace(', ',''))
	if multiplicand * multiplier == product:
		pandigitals.append(product)

# 2 digits * 3 digits = 4 digits
for num in all_p:
	multiplicand = int(str(num[:2]).strip('()').replace(', ',''))
	multiplier = int(str(num[2:5]).strip('()').replace(', ',''))
	product = int(str(num[5:10]).strip('()').replace(', ',''))
	if multiplicand * multiplier == product:
		pandigitals.append(product)

productlist = np.unique(pandigitals)
print sum(productlist)