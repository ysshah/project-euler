# What is the sum of the digits of the number 2^1000 ?

num = 2**1000
digit_sum = 0

for i in range(0,len(str(num))):
	digit_sum += int(str(num)[i])

print digit_sum