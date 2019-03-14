# baekjoon source = "https://www.acmicpc.net/problem/2477"
import sys


N = int(sys.stdin.readline())
go = '*'
result = []

idx = 0
while True:
    if 3 ** idx == N:
        k = idx
        break
    idx += 1

print(k)

for i in range(k):
    for j in range(3):
        result.append(go*3)
