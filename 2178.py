from collections import deque
from sys import stdin

def BFS(t, r, mazeSqure, queue):

    result = 0

    while queue:
        x, y = queue.popleft()
        if x == t - 1 and y == r - 1:
            mazeSqure[x][y] = mazeSqure[x][y] + 1
            # print(visited[x][y])
            break

        for j in range(4):
            mx, my = x + dx[j], y + dy[j]
            # print(mx, my)
            if 0 <= mx < t and 0 <= my < r and mazeSqure[mx][my] == 1:

                queue.append([mx, my])
                mazeSqure[mx][my] = mazeSqure[x][y] + 1
            else:
                continue

    for i in range(t):

        result = max(result, max(mazeSqure[i]))

    return result


# t, r = map(int, input().split())
t, r = map(int, stdin.readline().split())
# 지도 입력
mazeSqure = [list(map(int, input().split())) for _ in range(t)]
# mazeSqure1 = [stdin.readline().rstrip() for _ in range(t)]
# visited = [[0] * r for _ in range(t)]

print(mazeSqure)
# print(mazeSqure1)
# print(visited)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append([0, 0])

print(BFS(t, r, mazeSqure, queue) - 1)