# baekjoon source = "https://www.acmicpc.net/problem/1725"


def solution(l, r, m):
    global result

    print(l, r, m, result)
    result = max(result, min(arr[l:m]) * (m - l))
    print(result)
    result = max(result, min(arr[m:r]) * (r - m))
    print(result)
    result = max(result, min(arr[m:m+2])*2)
    print("result",result)
    c = m - 1
    b = (l + c) // 2
    if l != b and b != c:
        solution(l, c, b)

    a = m
    c = r
    b = (a + c) // 2
    if b != c and a != b:
        solution(a, c, b)

n = int(input())

arr = [int(input()) for _ in range(n)]
result = min(arr)*n
left = right = mid =  0

print(arr)
solution(0, n, n // 2)
print(result)
