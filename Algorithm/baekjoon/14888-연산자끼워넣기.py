# baekjoon source = "https://www.acmicpc.net/problem/14888"

def solution(idx, sum_):
    q = [[sum_, idx, [0] * (n - 1)]]
    max_ = float('-inf')
    min_ = float('inf')
    while q:
        t = q.pop(0)
        max_ = max(max_, t[0])
        min_ = min(min_, t[0])
        for i in range(idx, n):
            for j in range(n - 1):
                if not t[2][j]:
                    t[2][j] = 1
                    if method[j] == 1:
                        q.append([t[0] + number[i], t[2]])
                    elif method[j] == 2:
                        q.append([t[0] - number[i], t[2]])
                    elif method[j] == 3:
                        q.append([t[0] * number[i], t[2]])
                    else:
                        q.append([t[0] // number[i], t[2]])

    return [max_, min_]

n = int(input())
number = list(map(int, input().split()))
me = list(map(int, input().split()))
method = []
for i in range(len(me)):
    if me[i]:
        for j in range(me[i]):
            method.append((i + 1))

print(method)
print(n)
print(number)
print(me)

s = solution()
