# baekjoon source = "https://www.acmicpc.net/problem/2304"
'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

3
4 6
8 10
2 4

3
2 10
4 6
8 4
'''
import sys

N = int(sys.stdin.readline())
arr = [0]*N
result = 0
for i in range(N):
    L, H = map(int,sys.stdin.readline().split())
    arr[i] = (L,H)

arr.sort()
max_ = arr[0]
print(arr)
for i in range(1,N):
    if max_[1] > arr[i][1]:
        if i == N-1:
            result += (arr[i][0] - max_[0]+1)*arr[i][1]
            result += max_[1] - arr[i][1]
        elif i == 1:
            result += max_[1]

        if arr[i][1] == max(arr[i:][0]):
            max_ = arr[i]

    else:
        if i == N-1:
            result += (arr[i][0] - max_[0]) * max_[1]
            result += arr[i][1]
        else:
            result += (arr[i][0] - max_[0]) * max_[1]
            max_ = arr[i]

    print('r',result,max_)

print(result)
