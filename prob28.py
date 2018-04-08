
# 43 44 45 46 47 48 49 
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31

#Sum the diagonals of a 1001x1001 spiraling number series

ol = [1]
last = ol[-1]
dimension = 1001
stop = dimension**2

increaselen = 5
step = 2

while last < stop:
	ol.append(ol[-1] + step)
	last = ol[-1]
	newlen = len(ol)
	if newlen == increaselen:
		step += 2
		increaselen += 4

print sum(ol)