# baekjoon source = "https://www.acmicpc.net/problem/2661"

import sys

def backtracking(a,k,b):
    global flag
    c = [0] * 4
    if flag:
        if k == b:
            print(''.join(list(map(str,a[1:]))))
            flag = False
        else:
            k += 1
            candi = ncandi(a,k,b,c)
            for i in range(candi):
                a[k] = c[i]
                backtracking(a,k,b)

def ncandi(a,k,b,c):
    check = [0] * 4
    st, la = 1, k//2

    check[a[k-1]] = 1
    
    if k%2:
        st = 2
        if a[st:la] == a[st+la:st+la]:
            check[a[la]] == 1
    else:
        if a[st:la] == a[st+la:la+la]:
            check[a[la]] == 1

    print(check)
    candi = 0
    
    for i in range(1,4):
        if not check[i]:
            c[candi] = i
            candi += 1
    
    print('c',c)

    return candi

N = int(sys.stdin.readline())
a = [0]*(N+1)
flag = True

backtracking(a,0,N)

