import sys

sys.stdin = open("3752_가능한시험점수.txt", "r")

def bfs(x):
    pass

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    arr = [[0] * n for _ in range(n)]
    idx = 1
    result = []

    for i in range(n):
        idx += i
        while idx < n:
            result.append(score[idx])
            idx += 1


    print(result)
    print(len(result))
    print(score)

    for i in arr:
        print(i)

    print(n, score)
