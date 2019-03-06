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
arr = [[0] * (y) for _ in range(x)]
max_,y_m = 0,0
memo = []

for i in range(cnt):
    dot, num = map(int, sys.stdin.readline().split())
    if (dot, num) not in memo:
        if dot == 0:
            arr.insert(num+1,[0]*len(arr[0]))
            for j in range(len(arr[0])):
                if arr[num][j] == 1:
                    if num+1 <= len(arr)-1:
                        arr[num+1][j] = 1
                arr[num][j] = 1
        else:
            for a in range(len(arr)):
                arr[a].insert(num+1,0)
            for j in range(len(arr)):
                if arr[j][num] == 1:
                    if num + 1 <= len(arr[0]) - 1:
                        arr[j][num+1] = 1
                arr[j][num] = 1

    for i in arr:
        print(i)
    print()

    memo.append((dot,num))

cou = 0
for a in range(len(arr[0])):
    if arr[0][a] == 0:
        cou += 1
    else:
        max_ = max(max_,cou)
        cou = 0
max_ = max(max_, cou)

cou = 0
for a in range(len(arr)):
    if arr[a][0] == 0:
        cou += 1
    else:
        y_m = max(y_m,cou)
        cou = 0
y_m = max(y_m,cou)

print(max_*y_m)