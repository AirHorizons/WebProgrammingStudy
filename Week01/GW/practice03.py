import timeit
def isPrime(n):
    n2=int(n**0.5)
    if n % 2 == 0:
        print(False)
        return
    for i in range(3, n2+1, 2) :
        if n % i == 0 :
            print(False)
            break
    else:
        print(True)

t1 = timeit.timeit('isPrime(18014398241046527)', setup = 'from __main__ import isPrime', number = 1)
print(t1)
# 제곱근 만세!
# indent가 잘못되어 있었군요.... ㅜㅠㅠ,.....
