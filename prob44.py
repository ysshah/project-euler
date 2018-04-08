pent = set(n * (3*n - 1) / 2 for n in range(1,10000))
diffs = set()

for j in pent:
	for k in pent:
		if j + k in pent:
			if abs(k - j) in pent:
				diffs.add(abs(k - j))

print('answer =', int(min(diffs)))