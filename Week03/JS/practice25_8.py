keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

del x['delta']
p = [k for k, v in x.items() if v == 30]
for i in p:
    del x[i]
print(x)