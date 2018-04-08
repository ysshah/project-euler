import math
answerlist = []

for i in range(1,100000):
	num = i
	factlist = [math.factorial(int(x)) for x in str(num)]
	fact = sum(factlist)
	if num == fact:
		answerlist.append(num)

print answerlist