def check_arrival(start):
	global eightynine_sum, eightynine_set
	startset = set()
	startset.add(start)
	while start != 1:
		if start in eightynine_set:
			eightynine_sum += 1
			return
		if start == 89:
			for s in startset:
				eightynine_set.add(s)
			eightynine_sum += 1
			return
		start = sum(int(n)**2 for n in str(start))
		startset.add(start)

eightynine_set = set()
eightynine_sum = 0

for i in range(1,10000000):
	print(i)
	check_arrival(i)

print('answer = ', eightynine_sum)