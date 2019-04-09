# baekjoon source = "https://www.acmicpc.net/problem/17136"

def check(x):
    if x > 9: return False
    return True

def solution(x, y, sum_):
    global result



    for i in range(x,10):
        for j in range(y,10):
            if arr[i][j] == 1:
                for z in range(4, 0, -1):
                    if check(i + z) and check(j + z) and visited[z] <= 3:
                        flag = True
                        for a in range(i, i + z):
                            if flag:
                                for b in range(j, j + z):
                                    print(a,b,z)
                                    if arr[a][b] != 1:
                                        flag = False
                                        break
                            else:
                                break

                    if flag:
                        print('asdfasdf',z)
                        visited[z] += 1
                        for a in range(i, i + z):
                            for b in range(j, j + z):
                                arr[a][b] = 2
                        if check(y+1):
                            solution(x,y+1,sum_+1)
                        else:
                            solution(x+1,0,sum_+1)
                        for a in range(i, i + z):
                            for b in range(j, j + z):
                                arr[a][b] = 1

    for xxx in arr:
        print(xxx)
    print()


arr = [list(map(int, input().split())) for _ in range(10)]
visited = [0] * 5
result = 99999999

solution(0, 0, 0)
print(result)
