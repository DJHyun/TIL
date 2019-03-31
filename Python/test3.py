'''
3
3
2 2 2 2 5 0
3 3 3 3 1 0
4
1 1 3 5 3 9 4 1
9 1 11 0 0 4 7 8
4
1 1 3 3 5 5 7 7
2 2 4 4 6 6 8 8
1
10
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100
'''

def check(x, y):
    if x < 0 or x > 101 - 1: return False
    if y < 0 or y > 101 - 1: return False
    if visited[x][y] == 1: return False
    return True

def solution(x, y, idx):
    tq = []
    tq.append([x, y])
    cnt = -1
    while tq:
        q = tq[:]
        tq = []
        cnt += 1
        while q:
            t = q.pop(0)
            if arr[t[0]][t[1]] == 3:
                result[idx].append([cnt, t[0], t[1]])

            visited[t[0]][t[1]] = 1
            for i in range(4):
                if check(t[0] + dx[i], t[1] + dy[i]):
                    visited[t[0] + dx[i]][t[1] + dy[i]] = 1
                    tq.append([t[0] + dx[i], t[1] + dy[i]])

def gogo(d, result, sum_):
    global ans, n

    if sum_ >= ans:
        return

    if d == n:
        ans = min(ans, sum_)

    for i in range(n):
        if not vi[i]:
            vi[i] = 1
            gogo(d + 1, result, sum_ + result[d][i][0])
            vi[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0] * 101 for _ in range(101)]
    food = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    result = [[] for _ in range(n)]
    idx = -1
    vi = [0] * n
    ans = 9999999

    for i in range(0, n * 2, 2):
        arr[food[i]][food[i + 1]] = 3
        arr[robot[i]][robot[i + 1]] = 2

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                idx += 1
                visited = [[0] * 101 for _ in range(101)]
                solution(i, j, idx)

    for i in range(n):
        result[i] = sorted(result[i], key=lambda x: (x[1], x[2]))

    print(result)
    gogo(0, result, 0)
    print(f'#{test_case} {ans}')
