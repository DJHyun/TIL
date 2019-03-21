import sys

sys.stdin = open("1242_암호코드스캔.txt", "r")

def remove_zero(a):
    global m

    for i in range(len(a)):
        idx = 0
        mdx = m
        while idx < mdx:
            if check_arr[i][idx] == '0':
                check_arr[i].pop(idx)
                mdx -= 1
            else:
                idx += 1

        check_arr[i] = ''.join(check_arr[i])

def trans(a):
    for i in range(len(a)):
        a[i] = int(a[i], 16)
        a[i] = list(bin(a[i]))
        a[i].remove('b')

        while a[i][len(a[i]) - 1] != '1':
            a[i].insert(0, a[i].pop())

    return a

def check_len(a):
    global c
    for i in range(len(a)):
        if len(a[i]) >= 280:
            c = 5
            pass
        elif len(a[i]) >= 112:
            c = 2
            pass
        else:
            print(test_case, a[i], len(a[i]))
            c = 1
            while len(a[i]) > 56:
                a[i].pop(0)

        return a

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    print(n,m)
    arr = [list(input()) for _ in range(n)]
    check_arr = []
    c = 0

    for i in arr:
        if i.count('0') < m and i not in check_arr:
            check_arr.append(i)

    number = [[]] * len(check_arr)

    print(check_arr)
    remove_zero(check_arr)
    check_arr = trans(check_arr)
    check_arr = check_len(check_arr)

    print(check_arr)
    check = ['000' * c + '11' * c + '01' * c, '00' * c + '11' * c + '00' * c + '1',
             '00' * c + '1' * c + '00' * c + '11' * c,
             '0' * c + '1111' * c + '0' * c + '1' * c, '0' * c + '1' * c + '000' * c + '11' * c,
             '0' * c + '11' * c + '000' * c + '1' * c,
             '0' * c + '1' * c + '0' * c + '1111' * c, '0' * c + '111' * c + '0' * c + '11' * c,
             '0' * c + '11' * c + '0' * c + '111' * c,
             '000' * c + '1' * c + '0' * c + '11' * c]

    for i in range(len(check_arr)):
        for j in range(0, len(check_arr[i]), 7 * c):
            print(check_arr[i][j:j + 7 * c])
            if ''.join(check_arr[i][j:j + 7 * c]) in check:
                number[i].append(check.index(''.join(check_arr[i][j:j + 7 * c])))

    result = 0
    for i in range(len(number)):
        odd, even = 0, 0
        for j in range(7):
            if j % 2:
                even += number[i][j]
            else:
                odd += number[i][j]

        print(odd, even, number[i][7])
        if not (odd * 3 + even + number[i][7]) % 10:
            result += odd + even + number[i][7]

    print(f'#{test_case} {result}')
    print(number)
