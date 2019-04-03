import sys

sys.stdin = open("1952_수영장.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    prices = list(map(int, input().split()))
    days = list(map(int, input().split()))
    result = 0
    r = [0] * 12
    top = -1

    result = []
    for i in range(12):
        result.append([])
        for j in range(3):
            if j == 0:
                result[i].append([days[i], days[i] * prices[j], j])
            if j == 1:
                result[i].append([days[i], prices[j], j])
            if j == 2:
                result[i].append([days[i], prices[j], j])
        top += 1
        result[i] = sorted(result[i], key=lambda x: x[1])
        r[top] = result[i][0]

    result = 0
    for i in range(12):
        if r[i][2] == -1 or r[i][0] == 0:
            continue

        if r[i % 12][1] + r[(i + 1) % 12][1] + r[(i + 2) % 12][1] > prices[2] or r[i % 12][2] == 2:

            result += prices[2]

            if i == 10 and r[0][2] != -1:
                result -= r[0][1]
            if i == 11 and r[0][2] != -1:
                result -= r[0][1]
            if i == 11 and r[1][2] != -1:
                result -= r[1][1]

            r[i % 12][2] = -1
            r[(i + 1) % 12][2] = -1
            r[(i + 2) % 12][2] = -1
        else:
            result += r[i][1]
    print(r)

    print(f'#{test_case} {min(prices[3],result)}')
