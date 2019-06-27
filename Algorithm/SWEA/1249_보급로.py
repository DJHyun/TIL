# import sys
#
# sys.stdin = open('input.txt', 'r')

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

def dfs(a, b, sum_):
    print(a,b,sum_)
    global result

    if sum_ >= result:
        return 0

    for i in visited:
        print(i)
    print()
    for i in range(4):
        tx = a + dx[i]
        ty = b + dy[i]
        if tx == n - 1 and ty == n - 1:
            result = min(result,sum_)
            return 0
        if check(tx, ty) and not visited[tx][ty]:
            visited[tx][ty] = 1
            dfs(tx, ty, sum_+arr[tx][ty])
            visited[tx][ty] = 0


def bfs():
    q = [[0, 0, 0, 1]]
    min_result = float('inf')
    idx = 1
    visited[0][0] = idx
    while q:
        # print(q)
        t = q.pop(0)
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if tx == n - 1 and ty == n - 1:
                min_result = min(min_result, t[2])
                return min_result
            if check(tx, ty):
                q.append([tx, ty, t[2] + arr[tx][ty], idx])
                visited[tx][ty] = idx

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    result = float('inf')

    print(n)
    for i in arr:
        print(i)

    dfs(0,0,0)
    print(f'#{test_case} {result}')
