import sys

'''
10 8
3
0 3
1 4
0 2
'''
y, x = map(int, sys.stdin.readline().split())
cnt = int(sys.stdin.readline())
arr = [[0] * (y + 1) for _ in range(x + 1)]
x_len = [x]
y_len = [y]
sq = []

for i in range(cnt):
    dot, num = map(int, sys.stdin.readline().split())

    print(dot, num)

    if dot == 0:
        if i == 0:
            for j in range(i, len(x_len)):
                x_len.append(x_len[j] - num)
                y_len.append(y_len[j])
                x_len.append(num)
                y_len.append(y_len[j])
        else:
            for j in range(1 + (i - 1) * 2, len(x_len)):
                x_len.append(x_len[j] - num)
                y_len.append(y_len[j])
                x_len.append(num)
                y_len.append(y_len[j])
    else:
        if i == 0:
            for j in range(i, len(y_len)):
                y_len.append(y_len[j] - num)
                x_len.append(x_len[j])
                y_len.append(num)
                x_len.append(x_len[j])
        else:
            for j in range(1 + (i - 1) * 2, len(y_len)):
                y_len.append(y_len[j] - num)
                x_len.append(x_len[j])
                y_len.append(num)
                x_len.append(x_len[j])

    for j in range(len(x_len)):
        print(x_len[j], y_len[j])

    if dot == 0:
        for j in range(y + 1):
            if arr[num][j] == 1:
                arr[num][j] += 1
            else:
                arr[num][j] = 1
    else:
        for j in range(x + 1):
            if arr[j][num] == 1:
                arr[j][num] += 1
            else:
                arr[j][num] = 1

    for i in arr:
        print(i)
    print()
