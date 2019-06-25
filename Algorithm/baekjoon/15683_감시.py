# baekjoon source = "https://www.acmicpc.net/problem/15683"
def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] == 6: return False
    return True

def solution(v, x, y):
    q = [[x, y,0]]
    while q:
        t = q.pop(0)
        if v == 1:
            for i in range(4):
                tx = t[0] + dx[v - 1][i]
                ty = t[1] + dy[v - 1][i]
                if check(tx, ty):
                    q.append([tx,ty,t[2]])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [[[0] * n, [0] * n, [1] * n, [-1] * n]]
dy = [[[1] * n, [-1] * n, [0] * n, [0] * n]]
print(dx[0])
print(dx[0][1])
print(n, m)
for i in arr:
    print(i)

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 or arr[i][j] != 6:
            solution(arr[i][j], i, j)
