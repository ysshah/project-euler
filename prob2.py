import numpy as np

terms = [1, 2]

i = 1
nextterm = 3

while nextterm < 4000000:
	prevterm = terms[i]
	prevprevterm = terms[i-1]
	thisterm = prevterm + prevprevterm
	terms.append(thisterm)
	i += 1
	nextterm = thisterm + prevterm

# Two methods from here:

#### Make array of booleans, call them in original list
booleans = [x % 2 == 0 for x in terms]
newlist = np.array(terms)[np.array(booleans)]
print sum(newlist)

#### If each term is divisible by two, add it to a list and sum it up
newlist2 = []
for x in terms:
	if x % 2 == 0:
		newlist2.append(x)
print sum(newlist2)