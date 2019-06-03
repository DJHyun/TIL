# baekjoon source = "https://www.acmicpc.net/problem/16235"
'''
5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 7
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

10 1 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1

2 1 2
0 100
0 0
1 2 5
'''

def check(x, y):
    global n
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

n, m, k = map(int, input().split())
arr = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] * n for _ in range(n)]
add_arr = [list(map(int, input().split())) for _ in range(n)]
tree = [[0] * 3 for _ in range(m)]
print(arr)
for i in arr:
    print(i)
print()
for i in range(m):
    tree_input = list(map(int, input().split()))
    tree_input[0] -= 1
    tree_input[1] -= 1
    print(tree_input[2])
    print(arr[tree_input[0]][tree_input[1]][tree_input[2]])
    arr[tree_input[0]][tree_input[1]][tree_input[2]] += 1
# tree = [list(map(int, input().split())) for _ in range(m)]
tree = sorted(tree, key=lambda x: x[2])
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

print(n, m, k)

for i in add_arr:
    print(i)
print()

for i in tree:
    print(i)
print()
#
# idx = 0
# while idx < k:
#     # 봄
#     for i in range(m):
#         if not tree[i][3]:
#             if arr[tree[i][0]][tree[i][1]] >= tree[i][2]:
#                 arr[tree[i][0]][tree[i][1]] -= tree[i][2]
#                 tree[i][2] += 1
#             else:
#                 tree[i][3] = 1
#
#     # for i in arr:
#     #     print(i)
#     # print()
#     # for i in tree:
#     #     print(i)
#     # print()
#
#     # 여름
#     for i in range(m):
#         if tree[i][3]:
#             arr[tree[i][0]][tree[i][1]] += tree[i][2] // 2
#
#     # for i in arr:
#     #     print(i)
#     # print()
#
#     # 가을
#     new_tree = 0
#     for mix in range(m):
#         mix += new_tree
#         if not tree[mix][3] and not tree[mix][2] % 5:
#             for j in range(8):
#                 tx = tree[mix][0] + dx[j]
#                 ty = tree[mix][1] + dy[j]
#                 if check(tx, ty):
#                     tree.insert(0,([tx, ty, 1, 0]))
#                     mix += 1
#                     new_tree += 1
#                     m += 1
#
#
#     # for i in arr:
#     #     print(i)
#     # print()
#     # for i in tree:
#     #     print(i)
#     # print()
#
#     # 겨울
#     for i in range(n):
#         for j in range(n):
#             arr[i][j] += add_arr[i][j]
#
#     # for i in arr:
#     #     print(i)
#     # print()
#     # for i in tree:
#     #     print(i)
#
#     idx += 1
#
#     print(m,idx)
#
# result = 0
# for i in range(m):
#     if not tree[i][3]:
#         result += 1
# print(result)
