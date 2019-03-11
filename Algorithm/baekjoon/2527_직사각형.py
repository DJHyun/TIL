# baekjoon source = "https://www.acmicpc.net/problem/2527"
'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600

35 56 67 90 67 100 500 600
10 10 20 20 15 15 16 16
1 1 5 5 5 5 10 10
1 1 5 5 5 3 10 10

1 1 2 2 0 0 1 1
1 1 5 5 10 10 11 11
10 10 11 11 1 1 5 5
1 1 5 5 4 5 10 10

4 3 10 20 1 1 4 3
5 9 20 30 20 30 100 100
5 9 20 20 5 9 20 20

1 1 3 3 3 4 7 9
1 1 4 3 3 3 7 9
1 1 3 3 3 4 7 9
1 1 4 3 3 3 7 9
'''
import sys

for test_case in range(1, 5):
    num = list(map(int, sys.stdin.readline().split()))
    one = [num[:2], num[2:4]]
    two = [num[4:6], num[6:]]
    print(one, two)
    print(num)
    if one[0][0] > two[1][0] or one[0][1] > two[1][1] or one[1][0] < two[0][0] or one[1][1] < two[0][1]:
        print('d')
    elif one[1][0] == two[0][0] and one[0][1] < two[1][1]:
        print('b')
    elif one[1][1] == two[0][1] and one[0][0] < two[1][0]:
        print('b')
    elif one[0][0] == two[1][0] and one[1][1] > two[0][1]:
        print('b')
    elif one[0][1] == two[1][1] and one[0][0] < two[1][0]:
        print('b')
    elif one[1][0] == two[0][0] or one[1][1] == two[0][1] or one[0][0] == two[1][0] or one[0][1] == two[1][1]:
        print('c')
    else:
        print('a')

