
#for i in range(1, 101):
#    if i % 2 == 0 and i % 11 == 0:
#        print('FizzBuzz')
#    elif i % 2 == 0:
#        print('Fizz')
#    elif i % 11 == 0:
#        print('Buzz')
#    else:
#        print(i)

#실습문제

a, b = input().split()
if a > b:
    print('a는 b보다 작게 입력하세요!')
else:
    if (1<=a<=1000 and 10<=b<=1000):
        a = int(a)
        b = int(b)
    else:
        print('a는 1~1000, b는 10~1000 범위')
for i in range(a, b):
    if i % 5 == 0 and i % 7  == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 ==0:
        print('Buzz')
    else:
        print(i)