# baekjoon source = "https://www.acmicpc.net/problem/1003"

import sys

def dp(n):
    global one, two
    if n == 0:
        one += 1
        return 1

    if n == 1:
        two += 1
        return 1

    if memo[n] != 0:
        return memo[n]

    print(n)
    memo[n] = dp(n - 1) + dp(n - 2)
    print('m', n, memo[n])

    return memo[n]

T = int(sys.stdin.readline())

for test_case in range(T):
    num = int(sys.stdin.readline())
    memo = [0] * (num + 1)
    one, two = 0, 0
    dp(num)

    print(memo)
    print(f'#{test_case} {one} {two}')
