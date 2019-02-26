import sys
sys.stdin = open("Contact.txt", "r")

def bfs(start):
    result = 0
    tq = []
    visited = [0]*(max(node)+1)
    tq.append(start)
    visited[start] = 1
    while tq:
        q = tq[:]
        tq = []
        result = max(q)
        while q:
            t = q.pop(0)
            for i in range(len(matrix[t])):
                if matrix[t][i] == 1 and not visited[i]:
                    tq.append(i)
                    visited[i] = 1
    
    return result
 
for test_case in range(1, 2):
    len_, start = map(int,input().split())
    node = list(map(int,input().split()))
    matrix = [[0]*(max(node)+1) for _ in range(max(node)+1)]
 
    for i in range(0,len_,2):
        matrix[node[i]][node[i+1]] = 1
 

    for i in matrix:
        print(i)
    print(f'#{test_case} {bfs(start)}')