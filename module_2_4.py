numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0 #делители
for i in range(2, 16):
    for j in range (2, i):
        if i % j == 0:
            not_primes.append(i)
            k += 1
    if k == 0:
        primes.append(i)
    else:
        k = 0
print(primes)
not_primes_ = list(set(not_primes))
print(not_primes_)