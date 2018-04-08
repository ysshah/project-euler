# Find the sum of the digits in the number 100!

import math

num = math.factorial(100)
digit_sum = 0

for i in range(0,len(str(num))):
	digit_sum += int(str(num)[i])

print digit_sum