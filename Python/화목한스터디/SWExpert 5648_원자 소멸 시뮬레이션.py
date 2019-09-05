import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(float, input().split())) for _ in range(n)]
    result = 0
    cnt = n
    check = [0] * n

    while cnt > 1:
        dic = {}
        check_top = -1

        for i in range(n):
            if arr[i] == -1:
                continue

            if arr[i][2] == 0:
                arr[i][1] += 0.5
                if arr[i][1] == 1000:
                    arr[i] = -1
                    cnt -= 1
                else:
                    check_top += 1
                    check[check_top] = [i] + arr[i]
            elif arr[i][2] == 1:
                arr[i][1] -= 0.5
                if arr[i][1] == -1000:
                    arr[i] = -1
                    cnt -= 1
                else:
                    check_top += 1
                    check[check_top] = [i] + arr[i]
            elif arr[i][2] == 2:
                arr[i][0] -= 0.5
                if arr[i][0] == -1000:
                    arr[i] = -1
                    cnt -= 1
                else:
                    check_top += 1
                    check[check_top] = [i] + arr[i]
            else:
                arr[i][0] += 0.5
                if arr[i][0] == 1000:
                    arr[i] = -1
                    cnt -= 1
                else:
                    check_top += 1
                    check[check_top] = [i] + arr[i]

        for i in range(check_top + 1):
            flag = False
            if dic.get(str(check[i][1]) + '_' + str(check[i][2])) != None:
                if dic.get(str(check[i][1]) + '_' + str(check[i][2]))[2] == False:
                    dic.get(str(check[i][1]) + '_' + str(check[i][2]))[2] = True
                    flag = True
                cnt -= 1
                result += check[i][4]
                arr[check[i][0]] = -1
            else:
                dic[str(check[i][1]) + '_' + str(check[i][2])] = [check[i][0], check[i][4], False]

            if flag:
                cnt -= 1
                result += dic.get(str(check[i][1]) + '_' + str(check[i][2]))[1]
                arr[dic.get(str(check[i][1]) + '_' + str(check[i][2]))[0]] = -1

    print(f'#{test_case} {int(result)}')
