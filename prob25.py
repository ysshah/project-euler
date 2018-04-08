# What is the first term in the Fibonacci sequence to contain 1000 digits?

terms = [1, 1]

i = 1
nextterm = 3
digits = 0

while digits < 1000:
	prevterm = terms[i]
	prevprevterm = terms[i-1]
	thisterm = prevterm + prevprevterm
	terms.append(thisterm)
	i += 1
	nextterm = thisterm + prevterm
	digits = len(str(nextterm))

# Since i is the term that it stopped on, i + 1 is the term that is 1000 digits
# long ('nextterm'). Python is zero-based, so i + 2 is the 1000 digit term.
print i + 2