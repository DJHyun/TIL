# baekjoon source = "https://www.acmicpc.net/problem/10158"
'''
6 4
4 1
8
'''
import sys

w, h = map(int, sys.stdin.readline().split())
q, p = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
p_flag, q_flag = 1, 1

for i in range(t % (w * h)):
    if p + 1 > h:
        p_flag = 0
    elif p - 1 < 0:
        p_flag = 1

    if p_flag:
        p += 1
    else:
        p -= 1

    if q + 1 > w:
        q_flag = 0
    elif q - 1 < 0:
        q_flag = 1

    if q_flag:
        q += 1
    else:
        q -= 1

print(q, p)
