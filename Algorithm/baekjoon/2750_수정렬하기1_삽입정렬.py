# baekjoon source = "https://www.acmicpc.net/problem/2750"

import sys

n = int(sys.stdin.readline())
first = []
second = []

for test_case in range(n):
    num = int(sys.stdin.readline())
    first.append(num) if test_case == 0 else second.append(num)

for s_num in range(len(second)):
    for f_num in range(len(first)-1,-1,-1):
        if first[f_num] > second[s_num]:
            if f_num == 0:
                first.insert(f_num,second[s_num])
        else:
            if f_num == 0:
                first.insert(f_num+1,second[s_num])
        print(first[f_num],first,second)

print(first,second)
        
    
