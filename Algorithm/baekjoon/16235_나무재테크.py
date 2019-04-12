# baekjoon source = "https://www.acmicpc.net/problem/16235"
import time

def check(x, y):
    global n

    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

st = time.time()

n, m, k = map(int, input().split())
arr = [[5] * n for _ in range(n)]
value_arr = [list(map(int, input().split())) for _ in range(n)]
tree = []
for i in range(m):
    nn = list(map(int, input().split()))
    tree.append([nn[2], nn[0], nn[1]])

dx, dy = [1, 1, 1, -1, -1, -1, 0, 0], [1, 0, -1, 1, 0, -1, 1, -1]

for aa in range(k):
    print(aa)
    yang = []
    len_tree = len(tree)
    tree.sort()
    i = 0
    gogo = []

    while i < len_tree:

        if not arr[tree[i][1] - 1][tree[i][2] - 1]:
            yang.append(tree.pop(i))
            len_tree -= 1
        elif arr[tree[i][1] - 1][tree[i][2] - 1] >= tree[i][0]:
            arr[tree[i][1] - 1][tree[i][2] - 1] -= tree[i][0]
            tree[i][0] += 1
            if not tree[i][0] % 5:
                gogo.append(tree[i])
            i += 1
        else:
            yang.append(tree.pop(i))
            len_tree -= 1

    len_yang = len(yang)
    for i in range(len_yang):
        arr[yang[i][1] - 1][yang[i][2] - 1] += (yang[i][0] // 2)

    for i in range(len(gogo)):
        if not tree[i][0] % 5:
            for j in range(8):
                xx = (tree[i][1] - 1) + dx[j]
                yy = (tree[i][2] - 1) + dy[j]
                if check(xx, yy):
                    tree += [[1, xx + 1, yy + 1]]

    # print(tree)
    for i in range(n):
        for j in range(n):
            arr[i][j] += value_arr[i][j]

print(len(tree))
print(time.time() - st)
