# baekjoon source = "https://www.acmicpc.net/problem/1722"
import sys

def solution(k,number):
    global n, cnt


    if k == n:
        print(number)
        cnt += 1
        if m[0] == 1:
            if cnt == m[1]:
                print(' '.join(number))
                return True
        else:
            if number == str(m[1])+str(m[2])+str(m[3])+str(m[4]):
                print(cnt)
                return True

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            if solution(k+1, number+str(i)):
                break
            visited[i] = 0

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
visited = [0] * (n + 1)
cnt = 0

solution(0,'')
