'''
3
3 8
1 3 8 4 -3 -3 5 1
8 -2 5 5 4 -9 -8 -1
4 9 2 -1 0 4 3 2
3 8
4 0 1 -9 9 6 -5 -5
2 10 -8 6 9 -10 -3 0
9 5 -10 10 -9 -6 2 -8
3 8
-10 -5 8 1 -10 -3 -10 4
4 3 9 -6 -4 2 -3 -9
-4 7 10 3 1 5 9 1
'''

def solution(a, b, c):
    global n, m

    number = [0]*6
    idx = -1

    idx += 1
    sum_ = 0
    for i in range(a+1):
        for j in range(0,b+1):
            sum_ += arr[i][j]
    number[idx] = sum_

    idx += 1
    sum_ = 0
    for i in range(a+1):
        for j in range(b+1,c+1):
            sum_ += arr[i][j]
    number[idx] = sum_

    idx += 1
    sum_ = 0
    for i in range(a+1):
        for j in range(c+1,m):
            sum_ += arr[i][j]
    number[idx] = sum_

    idx += 1
    sum_ = 0
    for i in range(a+1,n):
        for j in range(0,b+1):
            sum_ += arr[i][j]
    number[idx] = sum_

    idx += 1
    sum_ = 0
    for i in range(a+1,n):
        for j in range(b+1,c+1):
            sum_ += arr[i][j]
    number[idx] = sum_

    idx += 1
    sum_ = 0
    for i in range(a+1,n):
        for j in range(c+1,m):
            sum_ += arr[i][j]
    number[idx] = sum_

    result = 0
    for i in range(6):
        for j in range(i+1,6):
            for z in range(j+1,6):
                sum_ = abs(number[i]-number[j])+abs(number[j]-number[z])+abs(number[z]-number[i])
                result = max(result,sum_)

    return result

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n-1):
        for j in range(m-1):
            for z in range(j+1,m-1):
                r = solution(i,j,z)
                ans = max(ans,r)

    print(f'#{test_case} {ans}')

