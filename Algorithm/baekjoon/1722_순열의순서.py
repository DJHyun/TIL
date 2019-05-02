# baekjoon source = "https://www.acmicpc.net/problem/1722"
import sys
import itertools

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

number = list(itertools.permutations(range(1,n+1)))
if m[0] == 1:
    print(' '.join(list(map(str,number[m[1]-1]))))
else:
    print(number.index(tuple(m[1:]))+1)


