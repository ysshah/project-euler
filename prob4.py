# Find largest palindrome product made from product of two 3 digit numbers

import numpy as np

mylist = []

for x in range(900,1000):
	for y in range(900,1000):
		mylist.append(x*y)

mylist = np.unique(mylist)

newlist = []
for k in mylist:
	first = str(k)[:3]
	last = str(k)[::-1][:3]
	if first == last:
		newlist.append(k)

print newlist