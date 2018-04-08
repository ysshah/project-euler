import numpy as np

mult = [1,2,3,4,5,6,7,8,9]
panlist = []
info = []

for i in range(1,10000):
	digits = ''
	for x in mult:
		digits += str(i*x)
		if len(digits) >= 9:
			check = ''.join(sorted(digits))
			if check == '123456789':
				panlist.append(int(digits))
				info.append([i,range(1,x+1)])
			break

panlist.sort()
print panlist[-1]
print info[-1]