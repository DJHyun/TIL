import sys

sys.stdin = open("3074_입국심사.txt", "r")

T = int(input())
for test_case in range(1, 2):
    n, m = map(int, input().split())
    one = int(input())
    two = int(input())
    check = 3
    if one > two:
        flag = True
    else:
        flag = False
    min_sum = 0

    for i in range(n, m):

        if i <= n - 1:
            if flag:
                min_sum += two
                flag = False
            else:
                min_sum += one
                flag = True
        else:
            if check > min(one, two):
                check = 0
                min_sum += one
                print(min_sum)
                flag = True
                continue

            if flag:
                min_sum += two
                flag = False
            else:
                min_sum += one
                flag = False

        check += abs(one - two)
        print(i, min_sum - 17, check)
