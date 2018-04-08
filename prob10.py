from prime_stuff import primes
import timeit

start = timeit.default_timer()

# ---------------------------------------------- #
print('answer =',sum(primes(2000000)))
# ---------------------------------------------- #

end = timeit.default_timer()
print('---> took', round(end - start, 3), 'seconds')