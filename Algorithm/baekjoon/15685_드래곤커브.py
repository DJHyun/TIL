# baekjoon source = "https://www.acmicpc.net/problem/8958"
'''
3
3 3 0 1
4 2 1 3
4 2 2 1
'''
import sys

N = int(sys.stdin.readline())
arr = [[0]*10 for _ in range(10)]

for i in range(N):
    y,x,d,g = map(int,sys.stdin.readline().split())
    result = []

    result.append((x,y))

    for i in range(2**g):
        if d == 0: 
            y = y + 1
            if (x,y) in result:
                y = y - 2
                result.append((x,y))
                d = 3
            else:
                result.append((x,y))
                d = 1
        elif d == 1: 
            x = x - 1
            if (x,y) in result:
                x = x + 2
                result.append((x,y))
                d = 0
            else:
                result.append((x,y))
                d = 2
        elif d == 2: 
            y = y - 1
            if (x,y) in result:
                y = y + 2
                result.append((x,y))
                d = 1
            else:
                result.append((x,y))
                d = 3
        elif d == 3: 
            x = x + 1
            if (x,y) in result:
                x = x - 2
                result.append((x,y))
                d = 2
            else:
                result.append((x,y))
                d = 0
    
    print(result)

    for i in arr:
        print(i)

