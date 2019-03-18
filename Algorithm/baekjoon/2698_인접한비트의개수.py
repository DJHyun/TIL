# baekjoon source = "https://www.acmicpc.net/problem/2698"

import sys

def dp(a):
    if a >= N:
        return 1
    
    


T = int(sys.stdin.readline())

for _ in range(T):
    N,K = map(int,sys.stdin.readline().split())
    num = [1]*N
    visited = [[-1]*2 for _ in range(N)]
