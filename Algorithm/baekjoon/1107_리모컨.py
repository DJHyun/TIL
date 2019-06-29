# baekjoon source = "https://www.acmicpc.net/problem/1107"
'''
5457
3
6 7 8

45
3
4 5 6

45
9
0 1 2 3 4 5 6 7 8
'''
import sys

N = sys.stdin.readline().strip()
M = int(sys.stdin.readline())
fun = list(range(0,10))
not_function = sys.stdin.readline().split()
for i in range(M):
    fun.remove(int(not_function[i]))


print(N,M)
print(fun)