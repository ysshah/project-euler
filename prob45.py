test = range(100000)

triangle = [n*(n+1)/2 for n in test]
pentagonal = [n*(3*n-1)/2 for n in test]
hexagonal = [n*(2*n-1) for n in test]

print set(triangle).intersection(pentagonal).intersection(hexagonal)