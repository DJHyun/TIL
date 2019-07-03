# baekjoon source = "https://www.acmicpc.net/problem/1773"
n, c = map(int, input().split())
fire = [int(input()) for _ in range(n)]

result = 0
for i in fire:
    result += c//i

print(result)
