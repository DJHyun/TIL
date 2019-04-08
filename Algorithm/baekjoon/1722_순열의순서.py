# baekjoon source = "https://www.acmicpc.net/problem/1722"

import sys

def fato(x):
    if x == 1:
        return 1
    return x * fato(x-1)



def solution(flag, k, check):
    global cnt



    if flag == 1:
        for i in range(check):
            a[check-i-1] = m[1]%(i+1)+1
            m[1] //= (i+1)
        print(a)

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
a = [0]*n
cnt = 0


print(n)
print(m)
if m[0] == 1:
    m[1] -= 1
    visited = [0] * (n + 1)
    solution(1, 0, n)
else:
    visited = [0] * (n + 1)
    solution(0, 0, n)

