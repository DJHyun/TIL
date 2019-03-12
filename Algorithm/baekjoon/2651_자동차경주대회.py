# baekjoon source = "https://www.acmicpc.net/problem/2651"
'''
140
5
100 30 100 40 50 60
5 10 4 11 7
'''


def dfs(number):
    global x,result

    for i in range(number+1,len(a)):
        if x > sum(a[number+1:i+1]):
            print(number,i)
            result.append(number)
            dfs(i)
            result.remove(number)

    print(result)

import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
result = []


dfs(0)
dfs(1)