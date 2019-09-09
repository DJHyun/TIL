import sys

sys.stdin = open('input.txt', 'r')

def check(x, y, score):

    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if visited[x][y]: return False
    if score[arr[x][y]] == 1: return False
    return True

def solution(x, y, a, b, depth, index, score):
    global result

    for i in range(4):
        if index.count(0) == 2:
            if index[0] >= 1 and (index[1] >= 1 or index[3] >= 1):
                if i == 0: continue
            if index[1] >= 1 and (index[0] >= 1 or index[2] >= 1):
                if i == 1: continue
            if index[2] >= 1 and (index[1] >= 1 or index[3] >= 1):
                if i == 2: continue
            if index[3] >= 1 and (index[0] >= 1 or index[2] >= 1):
                if i == 3: continue
        elif index.count(0) == 1:
            c = -1
            for cc in range(4):
                if index[cc] == 0:
                    c = cc
                    break
            if c == 0:
                if i == 2: continue
            if c == 1:
                if i == 3: continue
            if c == 2:
                if i == 0: continue
            if c == 3:
                if i == 1: continue


        tx = x + dx[i]
        ty = y + dy[i]
        if tx == a and ty == b and depth != 1 and result < depth+1:
            result = depth + 1
            # print('##############',result)
            return

        print(index)
        if i == 2:
            if index[0] == index[i]:
                continue
        if i == 3:
            if index[1] == index[i]:
                continue

        if check(tx, ty, score):
            index[i] += 1
            visited[tx][ty] = 1
            score[arr[tx][ty]] = 1
            solution(tx, ty, a, b, depth + 1, index, score)
            index[i] -= 1
            score[arr[tx][ty]] = 0
            visited[tx][ty] = 0




T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    result = -1
    dx, dy = [1, 1, -1, -1], [1, -1, -1, 1]

    for i in range(n):
        for j in range(n):
            visited = [[0] * n for _ in range(n)]
            visited[i][j] = 1
            sco = [0] * 101
            sco[arr[i][j]] = 1
            solution(i, j, i, j, 0, [0, 0, 0, 0], sco)

    print(f'#{test_case} {result}')
