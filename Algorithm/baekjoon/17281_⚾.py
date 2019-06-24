# baekjoon source = "https://www.acmicpc.net/problem/17281"
import itertools

n = int(input())
result = 0
human = [0] * 9
human[3] = 1
it = itertools.permutations(range(2, 10))

for i in it:
    idx = 0
    score = list(map(int, input().split()))
    base = [0, 0, 0]
    out = 0
    for j in i:
        if idx == 3:
            print(idx, j)
            flag = False
            idx += 1
            human[idx] = j
            idx += 1
            continue
        human[idx] = j
        idx += 1

    for h in range(9):
        if score[human[h]] == 1:
            for b in range(3):
                if base[b]:
                    if b + 1 >= 4:
                        score += 1
                    else:
                        base[b + 1] = 1
                    base[b] = 0
            base[0] = 1
        elif score[human[h]] == 2:
            for b in range(3):
                if base[b]:
                    if b + 2 >= 4:
                        score += 1
                    else:
                        base[b + 2] = 1
                    base[b] = 0
            base[1] = 1
        elif score[human[h]] == 3:
            for b in range(3):
                if base[b]:
                    if b + 3 >= 4:
                        score += 1
                    else:
                        base[b + 3] = 1
                    base[b] = 0
            base[3] = 1
        elif score[human[h]] == 4:
            score += (base.count(1) + 1)
            base = [0,0,0]
        else:
            out += 1

# for i in range(n):
#     base = [0,0,0]
#     out = 0
#     score = 0
#     taja = list(map(int,input().split()))
