T = int(input())

for t in range(T):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    cnt = y - x

    current = 1
    i = 2
    result = 1

    while current < cnt:
        current += i // 2
        i += 1
        result += 1
        print("i : {} current : {} result : {}".format(i, current, result))

    if current > cnt:
        result -= 1

    print(result)
