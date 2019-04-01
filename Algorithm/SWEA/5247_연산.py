import sys

sys.stdin = open("5247_연산.txt", "r")
T = int(input())

def bfs(x):
    global m, cnt
    tq = []
    tq.append(x)

    while tq:
        q = tq[:]
        tq = []
        while q:
            t = q.pop(0)
            visited[t] = 1
            for i in range(4):
                if i != 2:
                    if not visited[t + list_[i]] and t + list_[i] > 0:
                        tq.append(t + list_[i])
                        visited[t + list_[i]] = 1
                        if m == t + list_[i]:
                            return cnt
                else:
                    if not visited[t * 2] and t * 2 > 0:
                        tq.append(t * 2)
                        visited[t * 2] = 1
                    if m == t * 2:
                        return cnt
        cnt += 1

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    list_ = [1, -1, 2, -10]
    visited = [0] * 1000000
    cnt = 0
    bfs(n)
    print(f'#{test_case} {cnt+1}')
