ints = []
view_list = []

def check(num, exp_range):
	for e in exp_range:
		integer = n ** e
		if len(str(integer)) == e and integer not in ints:
			ints.append(integer)
			view_list.append([integer, n, e])

for n in range(1,22):
	check(n, range(22))

view_list.sort()

for item in view_list:
	print(item[1], '^', item[2], '=', item[0])

print('answer =', len(ints))