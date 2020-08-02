# 연습문제
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
# b = [i for i in range(len(a)) if len(i) == 5] # 제출한 정답
# b = [i for i in a if len(i) == 5] # 실제 정답
# print(b)

# 심사문제
a, b = map(int, input().split())
if a < b and 1 <= a <= 20 and 10 <= b <= 30:
    test = [2 ** i for i in range(a, b + 1)]
    del test[1]
    del test[-2]
    print(test)
