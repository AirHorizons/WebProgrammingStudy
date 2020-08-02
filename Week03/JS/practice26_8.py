#a = { i for i in range(100) if i%3 == 0}
#b = { k for k in range(100) if k%5 == 0}

#print(a & b)
c, d = map(int, input().split())
a = {i for i in range(1, c+1) if c % i == 0}
b = {k for k in range(1, d+1) if d % k == 0}
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)