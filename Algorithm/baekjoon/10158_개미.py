# baekjoon source = "https://www.acmicpc.net/problem/10158"
'''
6 4
4 1
8

0 1

6 4
4 1
7

0 1


40000 40000
0 0
200000000
'''

h, w = map(int, input().split())
q, p = map(int, input().split())
t = int(input())

print(w, h)
print(p, q)

xt = t % (2 * w)
xt, xd = xt % w, xt // w

xy = t % (2 * h)
xy, yd = xy % h, xy // h

print("asdfasdfasdf", xt, xd)
print('asdf', xy, yd)
p_flag, q_flag = 1, 1
for i in range(xt):
    if p + 1 > w:
        p_flag = 0
    elif p - 1 < 0:
        p_flag = 1

    if p_flag:
        p += 1
    else:
        p -= 1

for i in range(xy):
    if q + 1 > h:
        q_flag = 0
    elif q - 1 < 0:
        q_flag = 1

    if q_flag:
        q += 1
    else:
        q -= 1

print(p, q)
