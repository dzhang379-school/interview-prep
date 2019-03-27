import math
import time

def primes(a):

    primes = []

    for i in range(2, a):
        j = 1
        while j <= len(primes) and primes[j-1] <= math.sqrt(i):
            if i % primes[j-1] == 0:
                j = 0
                break
            j += 1
        if j:
            primes.append(i)
    return primes

def primes2(a):
    primes = list(range(2, a))
    i = 0
    while i < len(primes):
        primes = list(filter(lambda x: x % primes[i] != 0 and x != primes[i], primes))
    return primes


start = time.time()
print(primes(180))
print(time.time() - start)

start = time.time()
print(primes2(180))
print(time.time() - start)




