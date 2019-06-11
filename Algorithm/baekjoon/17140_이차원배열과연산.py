# baekjoon source = "https://www.acmicpc.net/problem/17140"

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
r -= 1
c -= 1
flag = True
result = 0
idx = 3

print(r, c, k)
for i in arr:
    print(i)

while arr[r][c] != k:
    if arr[r][c] > 100:
        break

    if flag:
        length = 0
        for i in range(len(arr)):
            make = {}
            for j in arr[i]:
                if j == 0:
                    continue
                if j not in make:
                    make[j] = 1
                else:
                    make[j] += 1
            length = max(length, len(make))
            make = sorted(make.items(), key=lambda x: (x[1], x[0]))
            arr[i] = []
            for j in make:
                arr[i] += j
    else:
        length = 0
        for i in range(len(arr)):
            make = {}
            for j in arr[i]:
                if j == 0:
                    continue
                if j not in make:
                    make[j] = 1
                else:
                    make[j] += 1
            length = max(length, len(make))
            make = sorted(make.items(), key=lambda x: (x[1], x[0]))
            arr[i] = []
            for j in make:
                arr[i] += j

    for i in range(len(arr)):
        if len(arr[i]) < (length * 2):
            arr[i] += ([0] * (length * 2 - len(arr[i])))

    for i in arr:
        print(i)

    if idx < (length * 2):
        idx = (length * 2)
        if flag:
            flag = False
        else:
            flag = True
    result += 1

print(result)
