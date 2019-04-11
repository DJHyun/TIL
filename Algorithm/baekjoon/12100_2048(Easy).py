# baekjoon source = "https://www.acmicpc.net/problem/1021"
import copy

'''
3
2 4 8
2 4 8
2 4 8
'''

def up(x):
    for j in range(n):
        i = 0
        while i < n - 1:
            if x[i][j] == x[i + 1][j]:
                x[i][j] += x[i + 1][j]
                flag = False
                for z in range(i + 1, n - 1):
                    flag = True
                    x[z][j] = x[z + 1][j]
                if flag:
                    x[z + 1][j] = 0

            elif x[i][j] == 0:
                flag = False
                for z in range(i, n - 1):
                    flag = True
                    x[z][j] = x[z + 1][j]
                if flag:
                    x[z + 1][j] = 0
                i -= 1

            i += 1

def down(x):
    for j in range(n):
        i = n - 1
        while i > 0:
            if x[i][j] == x[i - 1][j]:
                x[i][j] += x[i - 1][j]
                flag = False
                for z in range(i - 1, 0, -1):
                    flag = True
                    x[z][j] = x[z - 1][j]
                if flag:
                    x[z - 1][j] = 0

            elif x[i][j] == 0:
                flag = False
                for z in range(i , 0, -1):
                    flag = True
                    x[z][j] = x[z - 1][j]
                if flag:
                    x[z - 1][j] = 0
                i += 1

            i -= 1



def left(x):
    for j in range(n):
        i = 0
        while i < n - 1:
            if x[j][i] == x[j][i + 1]:
                x[j][i] += x[j][i + 1]
                flag = False
                for z in range(i + 1, n - 1):
                    flag = True
                    x[j][z] = x[j][z + 1]
                if flag:
                    x[j][z + 1] = 0
            elif x[j][i] == 0:
                flag = False
                for z in range(i , n - 1):
                    flag = True
                    x[j][z] = x[j][z + 1]
                if flag:
                    x[j][z + 1] = 0
                i -= 1

            i += 1

def right(x):
    for j in range(n):
        i = n - 1
        while i > 1:
            if x[j][i] == x[j][i - 1]:
                x[j][i] += x[j][i - 1]
                flag = False
                for z in range(i - 1, 0, -1):
                    flag = True
                    x[j][z] = x[j][z - 1]
                if flag:
                    x[j][z - 1] = 0
            elif x[j][i] == 0:
                flag = False
                for z in range(i , 0, -1):
                    flag = True
                    x[j][z] = x[j][z - 1]
                if flag:
                    x[j][z - 1] = 0
                i += 1

            i -= 1

def solution(a, k, check):
    global result

    for i in a:
        print(i)
    print()

    if k == check:
        max_ = 0
        for i in a:
            max_ = max(max_, max(i))
        result = max(max_, result)
        return 0

    for i in range(4):
        print(i)
        if i == 0:
            go = copy.deepcopy(a)
            up(go)
            solution(go, k + 1, check)
        elif i == 1:
            go = copy.deepcopy(a)
            down(go)
            solution(go, k + 1, check)
        elif i == 2:
            go = copy.deepcopy(a)
            left(go)
            solution(go, k + 1, check)
        else:
            go = copy.deepcopy(a)
            right(go)
            solution(go, k + 1, check)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

# print(n)
# for i in arr:
#     print(i)
# print()

solution(arr, 0, 5)
# for i in arr:
#     print(i)
# print()

print(result)
