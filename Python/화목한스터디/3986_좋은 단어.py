# baekjoon source = "https://www.acmicpc.net/problem/3986"

import sys

n = int(sys.stdin.readline())
result = 0

for a in range(n):
    s = sys.stdin.readline().strip()
    arr = ['']*4
    top = -1
    flag = True

    print(s)
    for i in range(len(s)):
        print(arr)
        if top == -1:
            top += 1
            arr[top] = s[i]
        elif top == 0:
            if arr[top] == s[i]:
                arr[top] = ''
                top -= 1
            else:
                top += 1
                arr[top] = s[i]
        elif top == 1:
            if arr[top] == s[i]:
                arr[top] = ''
                top -= 1
            else:
                top += 1
                arr[top] = s[i]
        else:
            if arr[top] == s[i]:
                arr[top] = ''
                top -= 1
            else:
                flag = False
                break

    else:
        if top != -1:
            flag = False

        if flag:
            result += 1
            print(a,s)
print(result)