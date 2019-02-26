import sys
sys.stdin = open("Contact.txt", "r")

def bfs(matrix,start):
    global result
    tq,f,r = [0],-1,-1

    r += 1
    tq[r] = start
    visited[start] = 1

    while f != r:
        q, qf, qr = tq[:],-1,r
        tq,f,r = [0]*len_,-1,-1
        result = max(q)
        while qf != qr:
            qf += 1
            t = q[qf]
            q[qf] = 0
            for i in range(len(matrix[t])):
                if matrix[t][i] == 1 and not visited[i]:
                    r += 1
                    tq[r] = i
                    visited[i] = 1

for test_case in range(1, 11):
    len_, start = map(int,input().split())
    node = list(map(int,input().split()))
    maxN = max(node)
    matrix = [[0]*(maxN+1) for _ in range(maxN+1)]
    visited = [0]*(maxN+1)
    result = 0

    for i in range(0,len_,2):
        matrix[node[i]][node[i+1]] = 1

    bfs(matrix,start)

    print(f'#{test_case} {result}')