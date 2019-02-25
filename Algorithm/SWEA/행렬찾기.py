import sys

sys.stdin = open("행.txt", "r")

T = int(input())

for test_case in range(1, 2):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = []
    check = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                if check != 0:
                    for z in range(i+1,n):
                        if arr[z][j-1] == 0:
                            result.append([z-i,check])
                            check = 0
                            break
                        else:
                            for b in range(check):
                                arr[z][j-1-b] = 0
            else:
                check += 1
                arr[i][j] = 0


    print(result)
    result = sorted(result, key=result[0]*result[1])
    print(result)
    
        