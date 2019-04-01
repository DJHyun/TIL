# baekjoon source = "https://www.acmicpc.net/problem/1722"

import sys

def solution(flag, k, check):
    global cnt

    if k == check:
        cnt += 1
        if a == m[1:]:
            print(cnt)
            return 0

    if flag:
        if cnt == m[1]:
            print(' '.join(map(str,a)))
            cnt += 1
            return 0

    for i in range(1, check + 1):
        if not visited[i]:
            visited[i] = 1
            a.append(i)
            fl = solution(flag, k + 1, check)
            if fl == 0:
                return 0
            a.pop()
            visited[i] = 0

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
a = []
cnt = 0

if m[0] == 1:
    visited = [0] * (n + 1)
    solution(1, 0, n)
else:
    visited = [0] * (n + 1)
    solution(0, 0, n)
