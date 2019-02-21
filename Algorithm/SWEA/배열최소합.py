import sys
sys.stdin = open("배열최소합.txt", "r")

def backtrack(a, k, input):
    global maxcandi
    c = [0] * maxcandi

    if k == input :
        for i in range(1, k+1):
            result.append(a[i])
    else:
        k += 1
        ncandi = construct(a, k, input, c)
        for i in range(ncandi):
            a[k] = c[i]
            backtrack(a, k, input)

def construct(a, k, input, c):
    global ncandi
    in_perm = [False]*input

    for i in range(1,k):
        in_perm[a[i]] = True
    
    ncandi = 0

    for i in range(0, input):
        if in_perm[i] == False:
            c[ncandi] = i
            ncandi += 1

    return ncandi

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ncandi , maxcandi = N, N
    a = [0] * (N+1)
    result = [[] for x in range(N+1) ]
    backtrack(a, 0, N)
    sum_,vsum = 9999,0

    arr = [list(map(int, input().split())) for x in range(N)]
    for i in arr:
        print(i)

    
    print(result)
    print(arr)
    print(sum_)
    