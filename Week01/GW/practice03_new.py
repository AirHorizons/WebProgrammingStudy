import timeit
import math
def isPrime(n):
    primes = [2]
    rt = int(math.sqrt(n))
    for i in range(2, rt+1):
        isIprime = True
        for prime in primes:
            if i % prime == 0:
                isIprime = False
                break
        if i != 2 and isIprime:
            primes.append(i)
    return primes
