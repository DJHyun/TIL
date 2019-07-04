# baekjoon source = "https://www.acmicpc.net/problem/10989"

import sys
import copy
def check(x, y):
    if x < 0 or x > N-1 : return False
    if y < 0 or y > M-1 : return False
    if arr[x][y] != 0  : return False
    return True

def bfs():
    q = []
    arr2 = copy.deepcopy(arr)
    visited = [[0]*M for _ in range(N)]
    result = 0

    for i in start:
        q.append(i)
        visited[i[0]][i[1]] = 1
    
    while q:
        t = q.pop(0)
        for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if check(x,y) and not visited[x][y]:
                    q.append((x,y))
                    visited[x][y] = 1
                    arr2[x][y] = 2
    

    for i in range(N):
        result += arr2[i].count(0)

    return result


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
a = [0] * 4
zero = 0
st = 0
dx, dy = [0,0,1,-1],[1,-1,0,0]
max_ = 0

for i in range(N):
    zero += arr[i].count(0)
    st += arr[i].count(2)
find, top = [0] * zero, -1
start, sop = [0] * st, -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            top += 1
            find[top] = (i,j)
        elif arr[i][j] == 2:
            sop += 1
            start[sop] = (i,j)

for i in range(0,zero):
    arr[find[i][0]][find[i][1]] = 3
    for j in range(i+1,zero):
        arr[find[j][0]][find[j][1]] = 3
        for a in range(j+1,zero):
            arr[find[a][0]][find[a][1]] = 3
            b = bfs()
            if max_ < b:
                max_ = b
            arr[find[a][0]][find[a][1]] = 0
        arr[find[j][0]][find[j][1]] = 0
    arr[find[i][0]][find[i][1]] = 0

print(max_)


