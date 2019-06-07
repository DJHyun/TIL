# baekjoon source = "https://www.acmicpc.net/problem/10158"
'''
6 4
4 1
8

0 1

40000 40000
0 0
200000000
'''

y, x = map(int, input().split())
q, p = map(int, input().split())
t = int(input())

# p_flag, q_flag = 1, 1
# for i in range(t % (w * h)):
#     if p + 1 > h:
#         p_flag = 0
#     elif p - 1 < 0:
#         p_flag = 1
#
#     if p_flag:
#         p += 1
#     else:
#         p -= 1
#
#     if q + 1 > w:
#         q_flag = 0
#     elif q - 1 < 0:
#         q_flag = 1
#
#     if q_flag:
#         q += 1
#     else:
#         q -= 1
#
# print(p, q)

print(x, y)
print(p, q)
print(t)

print(t % (x * 2))
print(t % (y * 2))
