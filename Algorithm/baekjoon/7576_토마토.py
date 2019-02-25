# baekjoon source = "https://www.acmicpc.net/problem/7576"
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''
import sys
def check(a,b):
    global M, N
    if a >= 0 and a < N and b >= 0 and b < M and tomato[a][b] == 0:
        return True
    return False


M, N = map(int,sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
idx = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt,ct = 0,-1


while True:

    visited = [[0] * M for _ in range(N)]
    if cnt == ct:
        idx -= 1
        break
    else:
        ct = cnt

    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1 and not visited[i][j]:
                for z in range(4):
                    x = i + dx[z]
                    y = j + dy[z]   
                    if check(x, y):
                        tomato[x][y] = 1
                        visited[x][y] = 1
                        cnt += 1
    
    idx += 1

flag = True
for i in tomato:
    if 0 in i:
        flag = False

if flag:
    print(idx)
else:
    print(-1)

