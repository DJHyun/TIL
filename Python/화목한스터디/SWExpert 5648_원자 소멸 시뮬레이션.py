import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    matrix = [[0] * 4000 for _ in range(4000)]

    for i in range(n):
        for j in range(2):
            arr[i][j] *= 2
        matrix[arr[i][0]][arr[i][1]] = 1

    result = 0
    cnt = n

    while cnt > 1:
        for i in range(n):
            if arr[i] == -1:
                continue

            if arr[i][2] == 0:
                if matrix[arr[i][0]][arr[i][1] + 1] == 0:
                    matrix[arr[i][0]][arr[i][1] + 1], matrix[arr[i][0]][arr[i][1]] = i, 0

            elif arr[i][2] == 1:
                if matrix[arr[i][0]][arr[i][1] - 1] == 0:
                    matrix[arr[i][0]][arr[i][1] - 1], matrix[arr[i][0]][arr[i][1]] = i, 0

            elif arr[i][2] == 2:
                if matrix[arr[i][0] - 1][arr[i][1]] == 0:
                    matrix[arr[i][0] - 1][arr[i][1]], matrix[arr[i][0]][arr[i][1]] = i, 0

            elif arr[i][2] == 3:
                if matrix[arr[i][0] + 1][arr[i][1]] == 0:
                    matrix[arr[i][0] + 1][arr[i][1]], matrix[arr[i][0]][arr[i][1]] = i, 0







    print(f'#{test_case} {int(result)}')
