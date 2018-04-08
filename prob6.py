# Find the difference between the sum of the squares of the first
# 100 natural numbers and the square of the sum

nums = range(1,101)

square_of_sums = sum(k for k in nums)**2
sum_of_squares = sum(k**2 for k in nums)

diff = square_of_sums - sum_of_squares

print diff