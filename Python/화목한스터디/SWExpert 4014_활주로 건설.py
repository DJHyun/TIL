import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    n, x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        check = []
        flag = False
        for j in range(n - 1):
            if arr[i][j] == arr[i][j + 1] + 1:
                if j + x < n:
                    check.append(j + 1)
                    for c in range(j + 2, j + x + 1):
                        if arr[i][j + 1] != arr[i][c] or c in check:
                            flag = True
                            break
                        else:
                            check.append(c)
                else:
                    flag = True

                if flag:
                    break

            elif arr[i][j] == arr[i][j + 1] - 1:
                if j - x + 1 > -1:
                    check.append(j)
                    for c in range(j - 1, j - x, -1):
                        if arr[i][j] != arr[i][c] or c in check:
                            flag = True
                            break
                        else:
                            check.append(c)
                else:
                    flag = True

                if flag:
                    break
            elif arr[i][j] != arr[i][j+1]:
                flag = True
                break
        if not flag:
            result += 1

    for i in range(n):
        flag = False
        check = []
        for j in range(n - 1):

            if arr[j][i] == arr[j + 1][i] + 1:
                if j + x < n:
                    check.append(j+1)
                    for c in range(j + 2, j + x + 1):
                        if arr[j + 1][i] != arr[c][i] or c in check:
                            flag = True
                            break
                        else:
                            check.append(c)
                else:
                    flag = True

                if flag:
                    break
            elif arr[j][i] == arr[j + 1][i] - 1:
                if j - x + 1 > -1:
                    check.append(j)
                    for c in range(j - 1, j - x, -1):
                        if arr[j][i] != arr[c][i] or c in check:
                            flag = True
                            break
                        else:
                            check.append(c)
                else:
                    flag = True

                if flag:
                    break

            elif arr[j][i] != arr[j+1][i]:
                flag = True
                break

        if not flag:
            result += 1
    print(f'#{test_case} {result}')
