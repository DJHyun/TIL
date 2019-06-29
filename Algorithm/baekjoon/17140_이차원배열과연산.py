# baekjoon source = "https://www.acmicpc.net/problem/17140"

# def change():
#     global arr
#     nArr = [[] for _ in range(y)]
#
#     for i in range(x):
#         for j in range(y):
#             nArr[j].append(arr[i][j])
#
#     arr = nArr
#
# r, c, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(3)]
#
# print(r, c, k)
# for i in arr:
#     print(i)
# print()
#
# x, y = 3, 3
# result = 0
# while True:
#     print(x, y, result, "번째")
#     for i in arr:
#         print(i)
#     print()
#     if r <= x - 1 and c <= y - 1:
#         if arr[r - 1][c - 1] == k:
#             break
#         if arr[r - 1][c - 1] == 100:
#             result = -1
#             break
#
#     if x >= y:
#         for i in range(x):
#             max_ = max(arr[i]) + 1
#             new = []
#             new_array = []
#             count = {}
#             for j in range(y):
#                 if arr[i][j] not in count:
#                     count[arr[i][j]] = 1
#                 else:
#                     count[arr[i][j]] += 1
#
#             for j in range(len(count)):
#                 if count[j]:
#                     new.append([j, count[j]])
#
#             new = sorted(new, key=lambda x: (x[1], x[0]))
#             for n in new:
#                 new_array += n
#             arr[i] = new_array
#
#         max_ = 0
#         for i in arr:
#             max_ = max(max_, len(i))
#
#         for i in range(x):
#             arr[i] += [0] * (max_ - len(arr[i]))
#         y = max_
#
#     else:
#         change()
#         for i in range(y):
#             max_ = max(arr[i]) + 1
#             new = []
#             new_array = []
#             count = [0] * max_
#             for j in range(x):
#                 count[arr[i][j]] += 1
#             for j in range(1, max_):
#                 if count[j]:
#                     new.append([j, count[j]])
#             new = sorted(new, key=lambda x: (x[1], x[0]))
#             for n in new:
#                 new_array += n
#             arr[i] = new_array
#
#         max_ = 0
#         for i in arr:
#             max_ = max(max_, len(i))
#
#         for i in range(y):
#             arr[i] += [0] * (max_ - len(arr[i]))
#
#         x = max_
#         x,y = y,x
#
#         change()
#
#         x, y = y, x
#
#     result += 1
#
# print(result)


def change():
    global arr

    new = [[0] * x for _ in range(y)]

    for i in range(y):
        for j in range(x):
            new[i][j] = arr[j][i]

    arr = new

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

x = 3
y = 3
result = 0
while True:

    if r <= x and c <= y:
        if arr[r - 1][c - 1] == k:
            break
        if result > 100:
            result = -1
            break

    if x >= y:
        max_len = 0
        for i in range(x):
            count_num = {}
            for j in range(y):
                if arr[i][j]:
                    if arr[i][j] not in count_num:
                        count_num[arr[i][j]] = 1
                    else:
                        count_num[arr[i][j]] += 1

            count_num = sorted(count_num.items(), key=lambda x: (x[1], x[0]))
            arr[i] = []
            for j in count_num:
                arr[i] += j
            max_len = max(max_len, len(arr[i]))

        for i in range(x):
            arr[i] += [0] * (max_len - len(arr[i]))

        y = max_len
    else:
        change()
        x, y = y, x
        max_len = 0

        for i in range(x):
            count_num = {}
            for j in range(y):
                if arr[i][j]:
                    if arr[i][j] not in count_num:
                        count_num[arr[i][j]] = 1
                    else:
                        count_num[arr[i][j]] += 1

            count_num = sorted(count_num.items(), key=lambda x: (x[1], x[0]))

            arr[i] = []
            for j in count_num:
                arr[i] += j
            max_len = max(max_len, len(arr[i]))

        for i in range(x):
            arr[i] += [0] * (max_len - len(arr[i]))



        y = max_len

        change()
        x,y = y,x

    result += 1

print(result)
