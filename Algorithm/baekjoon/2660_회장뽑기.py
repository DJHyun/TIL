# baekjoon source = "https://www.acmicpc.net/problem/2660"
'''
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1

2
1 2
-1 -1

3
1 2
2 3
-1 -1

5
1 2
2 3
3 4
4 5
-1 -1

6
1 2
2 3
3 4
4 5
5 6
2 4
2 5
-1 -1
'''
import sys

N = int(sys.stdin.readline())
arr = [[0] * (N + 1) for _ in range(N + 1)]
result = [0]
ans = []

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break

    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, N + 1):
    result.append(arr[i].count(0) - 1)

for i in arr:
    print(i)
print()
print(result)
print(min(result[1:]), result.count(min(result[1:])))

for i in range(1, N + 1):
    if min(result[1:]) == result[i]:
        ans.append(i)
ans.sort()

for i in ans:
    print(i, end=' ')
