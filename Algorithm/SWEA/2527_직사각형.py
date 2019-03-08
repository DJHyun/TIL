# baekjoon source = "https://www.acmicpc.net/problem/2527"
'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''
import sys

for test_case in range(1, 5):
    num = list(map(int, sys.stdin.readline().split()))
    one = num[:4];
    two = num[4:]
    one_one, one_two = [one[0], one[1]], [one[2], one[3]]
    two_one, two_two = [two[0], two[1]], [two[2], two[3]]

    if min(one) > max(two) or min(two) > max(one):
        print('d')
    elif (one_one == two_one and one_two != two_two) or (one_one == two_two) or (one_two == two_one) or (
            one_two == two_two):
        print('c')
    elif (one_two[0] == two_one[0] and one_two[1] > two_one[1]) or (
            one_two[1] == two_one[1] and one_two[0] > two_one[0]):
        print('b')
    else:
        print('a')
