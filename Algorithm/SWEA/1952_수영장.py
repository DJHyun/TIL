import sys

sys.stdin = open("1952_수영장.txt", "r")

T = int(input())
for test_case in range(1, 2):
    prices = list(map(int, input().split()))
    days = list(map(int, input().split()))
    result = 0
    check = [0] * 12
    top = -1

    result = []

    for i in range(12):
        result.append([])
        for j in range(3):
            if j == 0:
                result[i].append([days[i], days[i] * prices[j], j])
            if j == 1:
                result[i].append([days[i], prices[j], j])
        top += 1
        result[i] = sorted(result[i], key=lambda x: x[1])
        check[top] = result[i][0]

    result = 999999999
    for num in range(12):
        r = check[:]
        score = 0
        for i in range(12):
            print((i+num)%12)
            print()
            if r[(i + num) % 12][2] == -1 or r[(i + num) % 12][0] == 0:
                continue
            if ((i + num) % 12) < 10:
                if r[(i + num) % 12][1] + r[(i + num + 1) % 12][1] + r[(i + num + 2) % 12][1] > prices[2]:
                    score += prices[2]
                    r[(i + num + 1) % 12][2] = -1
                    r[(i + num + 2) % 12][2] = -1
                else:
                    score += r[(i + num) % 12][1]
            elif ((i + num) % 12) == 10:
                if r[(i + num) % 12][1] + r[(i + num + 1) % 12][1] > prices[2]:
                    score += prices[2]
                    r[11][2] = -1
                else:
                    score += r[(i + num) % 12][1]
            else:
                if r[(i + num) % 12][1] > prices[2]:
                    score += prices[2]
                else:
                    score += r[(i + num) % 12][1]

            # if score >= result:
            #     break
            print(score)
        result = min(score, result)

    print(f'#{test_case} {min(prices[3], result)}')
