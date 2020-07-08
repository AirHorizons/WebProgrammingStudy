def prime_number_generator(start, stop):
    num = start
    while num < stop:
        rt = int(num**0.5)
        isPrime = True
        for i in range(2, rt+1):
            if num % i == 0:
                isPrime = False
        if isPrime:
            yield num
        num += 1

start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
