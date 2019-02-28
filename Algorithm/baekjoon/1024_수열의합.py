# baekjoon source = "https://www.acmicpc.net/problem/1024"

import sys

def back(a,k,L):
    global N,result,ans,flag
    if k == 0:
        c = [0]*(N)
    else:
        c = [0]*2

    if flag:
        if k >= L and sum(a) == N:
            result = k
            ans = a[:]
        elif k > 100:
            a = [0] * (N+1)
            flag = False
        elif sum(a) < N:
            k += 1
            candi = cons(a,k,L,c)
            for i in range(candi):
                a[k] = c[i]
                back(a,k,L)
        elif sum(a) > N or k > result:
            for i in range(2,len(a)):
                a[i] = 0

def cons(a,k,L,c):
    if k == 1:
        candi = 0
        for i in range(1,N):
            c[candi] = i
            candi += 1
    else:
        candi = 0
        c[candi] = a[k-1]+1
        candi += 1

    return candi

    
N, L = map(int,sys.stdin.readline().split())
a = [0] * (N+1)
result = 0
ans = a[:]
flag = True

back(a,0,L)

if ans.count(0) == (N+1):
    print(-1)
else:
    for i in ans:
        if i != 0:
            print(i,end=' ')