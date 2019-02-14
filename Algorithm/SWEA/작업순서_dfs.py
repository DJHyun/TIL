import sys
sys.stdin = open("작업순서.txt", "r")


def dfs(v):
    global top

    if not visited[v]:
        top += 1
        stack[top] = v

    visited[v] = True

    for i in range(len(G)):
        if G[v][i] and not visited[i]:
            dfs(i)

    if v not in result:
        result.append(v)

for test_case in range(1, 11):
    num = list(map(int,input().split()))
    v, e = num[0],num[1]
    g = list(map(int,input().split()))[::-1]
    G = [[0]*(max(g)+1) for _ in range(max(g)+1)]
    visited, stack = [0]*(max(g)+1),[0]*(max(g)+1)
    st = 0
    result = []
    top = -1

    for a in range(0,len(g),2):
        G[g[a]][g[a+1]] = 1

    for i in range(len(G)):
        if i and not visited[i]:
            dfs(i)
    
    print(f'#{test_case} {" ".join(list(map(str,result)).strip())}')

