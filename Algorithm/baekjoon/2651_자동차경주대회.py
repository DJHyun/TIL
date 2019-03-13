# baekjoon source = "https://www.acmicpc.net/problem/2651"
'''
140
5
100 30 100 40 50 60
5 10 4 11 7

400
5
100 30 100 40 50 60
5 10 4 11 7

110
3
100 20 30 100
1 2 3

2
100
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

'''

def dfs(number, sum_):
    global x, n, result, num

    if number >= n+1:
        print(visited)
        if result == 0:
            result = 99999
            if result > sum_:
                result = sum_
                num = list(map(str,visited[:]))
                return
        else:
            if result > sum_:
                result = sum_
                num = list(map(str, visited[:]))
                return

    if sum_ > result and result != 0:
        return

    for i in range(1, n + 2):
        if i > number and dis[i] - dis[number] <= x and i not in visited:
            visited.append(i)
            dfs(i, sum_ + score[i])
            visited.pop(visited.index(i))

import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, 0)
score = list(map(int, sys.stdin.readline().split()))
score.insert(0, 0);score.append(0)
dis = [0] * len(arr)
visited = []
result = 0;
num = []

for i in range(1, len(arr)):
    dis[i] = sum(arr[:i + 1])

dfs(0, 0)

if result == 0:
    print(0)
else:
    num.pop()
    print(result)
    print(len(num))
    print(' '.join(num))
