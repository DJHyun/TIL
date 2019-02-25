# baekjoon source = "https://www.acmicpc.net/problem/25800"
'''
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''

import sys

number = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
check = [1,2,3,4,5,6,7,8,9]

for i in range(9):
    for j in range(9):
        flag = [True] * 10
        if number[i][j] == 0:
            for a in range(9):
                if number[i][a] in check:
                    flag[number[i][a]] = False
                if number[a][j] in check:
                    flag[number[a][j]] = False
                if i == 0 or i == 3 or i == 6:
                    if j == 0 or j == 3 or j == 6:
                        for b in range(1,3):
                            if number[i+b][j+b] in check:
                                flag[number[i][b]] = False
                            if number[i+b][j+3-b] in check:
                                flag[number[i+b][j+3-b]] = False
                    elif j == 1 or j == 4 or j == 7:
                        for b in range(1,3):
                            if number[i+b][j-1] in check:
                                flag[number[i+b][j-1]] = False
                            if number[i+b][j+1] in check:
                                flag[number[i+b][j-1]] = False
                    else:
                        for b in range(1,3):
                            if number[i+b][j-b] in check:
                                flag[number[i+b][j-b]] = False
                            if number[i+b][j-3+b] in check:
                                flag[number[i+b][j-3+b]] = False

                if i == 1 or i == 4 or i == 7:
                    if j == 0 or j == 3 or j == 6:
                        for b in range(1,3):
                            if number[i+b][j+b] in check:
                                flag[number[i][b]] = False
                            if number[i+b][j+3-b] in check:
                                flag[number[i+b][j+3-b]] = False
                    elif j == 1 or j == 4 or j == 7:
                        for b in range(1,3):
                            print(i+b, j-1)
                            if number[i+1][j-b%2+int(b/2)] in check:
                                flag[number[i+1][j-b%2+int(b/2)]] = False
                            if number[i-1][j-b%2+int(b/2)] in check:
                                flag[number[i-1][j-b%2+int(b/2)]] = False
                    else:
                        for b in range(1,3):
                            if number[i-b][j-b] in check:
                                flag[number[i+b][j-b]] = False
                            if number[i+b][j-3+b] in check:
                                flag[number[i+b][j-3+b]] = False
                
                else:
                    if j == 0 or j == 3 or j == 6:
                        for b in range(1,3):
                            if number[i+b][j+b] in check:
                                flag[number[i][b]] = False
                            if number[i+b][j+3-b] in check:
                                flag[number[i+b][j+3-b]] = False
                    elif j == 1 or j == 4 or j == 7:
                        for b in range(1,3):
                            if number[i+b][j-1] in check:
                                flag[number[i+b][j-1]] = False
                            if number[i+b][j+1] in check:
                                flag[number[i+b][j-1]] = False
                    else:
                        for b in range(1,3):
                            if number[i+b][j-b] in check:
                                flag[number[i+b][j-b]] = False
                            if number[i+b][j-3+b] in check:
                                flag[number[i+b][j-3+b]] = False


            for a in range(1,10):
                if flag[a]:
                    number[i][j] = a

for i in number:
    print(' '.join(map(str,i)))

            
                


