# baekjoon source = "https://www.acmicpc.net/problem/17136"

def check(x):
    if x > 9: return False
    return True

def solution(sum_, k, d, zz):
    global result

    print(visited)
    for ttt in arr:
        print(ttt)
    print()


    if result <= sum_:
        return

    if zz == 1:
        if d - k >= 5:
            return

    if k == d:
        result = min(result, sum_)

        return


    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                for z in range(5, 0, -1):
                    flag = True
                    if check(i + z - 1) and check(j + z - 1) and visited[z - 1] <= 4:
                        for a in range(i, i + z):
                            if flag:
                                for b in range(j, j + z):
                                    if arr[a][b] != 1:
                                        flag = False
                                        break
                            else:
                                break
                    else:
                        flag = False

                    if flag:
                        kk = 0
                        visited[z - 1] += 1
                        for a in range(i, i + z):
                            for b in range(j, j + z):
                                arr[a][b] = 2
                                kk += 1

                        solution(sum_ + 1, k + kk, d,z)

                        visited[z - 1] -= 1
                        for a in range(i, i + z):
                            for b in range(j, j + z):
                                # print(a,b)
                                arr[a][b] = 1

arr = [list(map(int, input().split())) for _ in range(10)]
vv = [[0] * 10 for _ in range(10)]
visited = [0] * 6
result = 99999999

d = 0
for i in arr:
    d += i.count(1)

solution(0, 0, d,0)
if result == 99999999:
    print(-1)
else:
    print(result)
