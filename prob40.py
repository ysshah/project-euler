nums = ''
for i in range(1,1000000):
	nums += str(i)

answer = 1
for i in [0,9,99,999,9999,99999,999999]:
	answer *= int(nums[i])

print answer