import itertools

p = itertools.permutations([0,1,2,3,4,5,6,7,8,9])
all_p = list(p)
numlist = []

for i in all_p:
	num = str(i).strip('()').replace(', ','')
	if int(num[1:4]) % 2 == 0:
		if int(num[2:5]) % 3 == 0:
			if int(num[3:6]) % 5 == 0:
				if int(num[4:7]) % 7 == 0:
					if int(num[5:8]) % 11 == 0:
						if int(num[6:9]) % 13 == 0:
							if int(num[7:10]) % 17 == 0:
								numlist.append(int(num))

print sum(numlist)