def solution(x, y):

    if y == 2:
        print(visited)
        return

    if x == 6:
        # print(visited)
        return

    visited[x] = 1
    solution(x + 1, y + 1)
    visited[x] = 0
    solution(x + 1, y)

visited = [0] * 6
solution(0, 0)
