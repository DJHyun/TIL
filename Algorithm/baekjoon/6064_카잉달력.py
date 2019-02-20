# baekjoon source = "https://www.acmicpc.net/problem/6064"
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    a,b,cnt = 1,1,1

    while M != a or b != N:

        if a < M:
            a += 1
        else:
            a = 1
        
        if b < N:
            b += 1
        else:
            b = 1
        
        cnt += 1
        print(a,b,cnt)
        if a == x and b == y:
            print(cnt)
            break
    else:
        print(-1)

    
    X = [M,x]; Y=[N,y]
    min_ = min(M,N)
    print(X,Y)
    a,b = 0, 0

    # if min_ in X:
    #     if (y - x) < 0:
    #         Y[1] = N - (y -x)
    #     else:
    #         Y[1] = y - x
    #     X[1] = M
        
    #     while Y[1] != N:
    #         N -= 2
    #         b += 1
        
    #     a = M*b

    #     while Y[1] 
        



    print(X,Y)