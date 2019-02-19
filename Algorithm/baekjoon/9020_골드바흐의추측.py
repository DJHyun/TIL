# baekjoon source = "https://www.acmicpc.net/problem/1929"
import sys
import math

T = int(sys.stdin.readline())

for test_case in range(T):
    n = int(sys.stdin.readline())
    number = [1]*(n+1)
    number[0], number[1] = 0,0
    sq = int(math.sqrt(n))

    j = 2
    for i in range(2,sq+1):
        if number[i]:
            while i*j < (n+1):
                number[i*j] = 0
                j += 1
    max_, min_ = 0,0

    for i in range(len(number)):
        if number[i]:
            if n-i in number:
                min_ = i
                max_ = n-i

    print(min_,max_)

    