def calc():
    value = 0
    while True:
        expr = (yield value)
        a, op, b = expr.split()
        if op == '+':
            value = int(a) + int(b)
        elif op == '-':
            value = int(a) - int(b)
        elif op == '*':
            value = int(a) * int(b)
        elif op == '/':
            value = int(a) / int(b)

expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()
