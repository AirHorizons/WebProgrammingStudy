r = int(input('반지름을 입력하시오: '))

for i in range(0,2*r+1):
    for j in range(0,2*r+1):
        if ((j-r)**2)+((i-r)**2)<=(r**2):
            print('*', end='')
        else:
            print(' ', end='')
    print()

