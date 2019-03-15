# baekjoon source = "https://www.acmicpc.net/problem/2477"
import sys

N = int(sys.stdin.readline())
result = [[' '] * N for _ in range(N)]

idx = 0
while True:
    if 3 ** idx == N:
        k = idx
        break
    idx += 1

check = []
idx = 0
jdx = 0

for a in range(2, k + 1):
    check.append([])
    for i in range(3 ** a // 3):
        check[idx].append((3 ** a // 3) + i)
        if 3 ** a != N:
            for j in range(N // (3 ** a) - 1):
                check[idx].append((check[idx][len(check[idx]) - 1] + 3 ** a))
            jdx += 1
    idx += 1

for i in range(N):
    for j in range(N):
        if i % 3 == 1:
            if j % 3 == 1:
                continue

        result[i][j] = '*'

        for a in range(2,k+1):
            if i //3**(a-1) == 1:
                if j //3**(a-1) == 1:
                    result[i][j] = ' '



for i in result:
    print(''.join(i))