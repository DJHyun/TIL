# baekjoon source = "https://www.acmicpc.net/problem/1107"
'''
5457
3
6 7 8

45
3
4 5 6

45
9
0 1 2 3 4 5 6 7 8
'''
import sys

N = sys.stdin.readline().strip()
M = int(sys.stdin.readline())
not_function = sys.stdin.readline().split()
fun = []

for i in range(0, 10):
    if str(i) not in not_function:
        fun.append(str(i))
min_ = abs(int(N) - 100)
max_ = abs(int(N) - 10 ** len(N)) + len(N) + 1
result = ''

if fun:

    for i in range(len(N)):
        if i == 0:
            if '0' in fun:
                fun.remove('0')
                flag = True

        if N[i] not in not_function:
            result += N[i]
        else:
            if i != len(N) - 1:
                mi = 10
                for j in fun:
                    if mi > abs(int(N[i]) - int(j)):
                        mi = abs(int(N[i]) - int(j))
                        re = j
                result += re
            else:
                ma = 500000
                for j in fun:
                    if ma > abs(int(N) - int(result + j)):
                        ma = abs(int(N) - int(result + j))
                        re = j
                result += re

        if flag:
            fun.append('0')

    print(result)
    min_for = abs(int(result) - int(N)) + len(result)

    if '0' in fun and '1' in fun:
        print(min(min_for, min_, max_))
    else:
        print(min(min_for, min_))
else:
    print(min_)
