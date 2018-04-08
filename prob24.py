# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order.
# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import itertools
import timeit

start = timeit.default_timer()

# ---------------------------------------------- #
p = itertools.permutations([0,1,2,3,4,5,6,7,8,9])
all_p = list(p)
all_p.sort()

print str(all_p[999999]).strip('()').replace(', ','')
# ---------------------------------------------- #

end = timeit.default_timer()
print('---> took', round(end - start, 3), 'seconds')