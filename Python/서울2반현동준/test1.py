'''
3
10
0 1 8 4
10
0 0 2 3
10
4 4 3 3
'''
def check(x, y):
    global n
    if x < 0 or x > n - 1: return
    if y < 0 or y > n - 1: return

    return True

def solution(x, y, sum_):
    global tx, ty, result

    if sum_ >= result:
        return

    if x == tx and y == ty:
        result = min(result, sum_)
        return sum_

    for i in range(8):
        if check(x + dx[i], y + dy[i]) and not arr[x + dx[i]][y + dy[i]]:
            arr[x + dx[i]][y + dy[i]] = 1
            solution(x + dx[i], y + dy[i], sum_ + 1)
            arr[x + dx[i]][y + dy[i]] = 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    y, x, ty, tx = map(int, input().split())
    result = 9999999999
    dx, dy = [2, 2, 3, 3, -2, -2, -3, -3], [-3, 3, -2, 2, 3, -3, -2, 2]

    solution(x, y, 0)
    print(f'#{test_case} {result}')
