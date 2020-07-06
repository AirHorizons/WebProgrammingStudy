def isPrime():
    n=int(input())
    n2=int(n**0.5)
    for i in range(2, n2+1) :
        if n % i == 0 :
            print(False)
            break
    else:
        print(True)

isPrime()

# 제곱근 만세!
# indent가 잘못되어 있었군요.... ㅜㅠㅠ,.....
