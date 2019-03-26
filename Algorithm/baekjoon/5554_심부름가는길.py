# baekjoon source = "https://www.acmicpc.net/problem/2935"

import sys

time_ = [0] * 4
for i in range(4):
    time_[i] = int(sys.stdin.readline())
x, y = 0, 0

for i in range(3):
    if y + time_[i] + time_[i + 1] >= 60:
        nn = (y)
        x += 1
        y += (time_[i] + time_[i + 1]) - 60
    else:
        y += time_[i] + time_[i + 1]

    print(x,y)
