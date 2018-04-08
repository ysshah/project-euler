import numpy as np

pythag = []
limit = 100
test_range = range(1,limit)

perimeter = np.zeros(shape=(1000,10),dtype=object)
perimeter[:,0] = range(1,1001)
amounts = []

# Define greatest common divisor function
def gcd(a, b):
	# Return greatest common divisor using Euclid's Algorithm.
	while b:
		a, b = b, a % b
	return a

# For every number in test_range (given a < b < c)
# If a^2 + b^2 = c^2 and if the GCD is 1, append triplet to pythag
for a in test_range:
	for b in range(a,limit):
		for c in range(b,limit):
			if c**2 == a**2 + b**2:
				if gcd(a,gcd(b,c)) == 1:
					pythag.append([a, b, c])

# For every triplet in pythag, multiply by range, check to see if it is = 1000
for i, p in enumerate(perimeter[:,0]):
	amt = 0
	for f in pythag:
		for mult in range(1,85):
			if sum(k*mult for k in f) == p:
				amt += 1
				this_triplet = [k*mult for k in f]
				perimeter[i,amt+1] = this_triplet
	perimeter[i,1] = amt

index = list(perimeter[:,1]).index(max(perimeter[:,1]))
print 'Perimeter = %i, Max Solutions = %i' %(perimeter[index,0], perimeter[index,1])
print 'Solutions = '
for k in perimeter[index,2:]:
	if k != 0:
		print '\t'+str(k)