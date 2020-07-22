"""
Practice of iterating loop and generator by generating primes with scope
"""
def prime_number_generator(start, stop):
    """
    Generates prime number from start to stop
    """
    num = start
    while num < stop:
        root = int(num**0.5)
        is_prime = True
        for i in range(2, root+1):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
        num += 1

_start, _stop = map(int, input().split())
g = prime_number_generator(_start, _stop)
print(type(g))
for j in g:
    print(j, end=' ')
