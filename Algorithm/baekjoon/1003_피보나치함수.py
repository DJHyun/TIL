# baekjoon source = "https://www.acmicpc.net/problem/1003"

import sys

def dp(n):
    if n == 1 or n == 0:
        return 1
    
    if memo[n] != 0:
        return memo[n]
    
    memo[n] = dp(n-1) + dp(n-2)

    return memo[n]

T = int(sys.stdin.readline())

for test_case in range(T):
    num = int(sys.stdin.readline())
    memo = [0]*num

    dp(num)
    print(memo)