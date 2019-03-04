# baekjoon source = "https://www.acmicpc.net/problem/8958"
'''
3
3 3 0 1
4 2 1 3
4 2 2 1
'''
import sys


def direction(x, y, d):
    if d == 0:
        y += 1
    elif d == 1:
        x -= 1
    elif d == 2:
        y -= 1
    else:
        x += 1

    return x, y


def turn(d):
    if d == 0:
        d = 1
    elif d == 1:
        d = 2
    elif d == 2:
        d = 3
    else:
        d = 0

    return d


N = int(sys.stdin.readline())
arr = [[0] * 10 for _ in range(10)]

for i in range(N):
    y, x, d, g = map(int, sys.stdin.readline().split())
    arr = [[0] * 10 for _ in range(10)]
    result = [[x, y]]
    dire = [d]

    idx = 0
    for i in range(g + 1):
        len_ = len(dire)
        for j in range(len_ - 1, -1, -1):
            if i == 0:
                x, y = direction(result[j][0], result[j][1], dire[j])
                result[0] += [x, y]
                result.append([x,y])
            else:
                d = turn(dire[j])
                dire.append(d)
                x, y = direction(result[idx][2], result[idx][3], d)
                idx += 1
                result[idx] += [x,y]
                result.append([x,y])

    print(result)