from collections import deque
from sys import stdin

t, r = map(int, stdin.readline().split())
# matrix 배열
mazeSqure = [stdin.readline().rstrip() for _ in range(t)]
# 방문경로 배열
visited = [[0] * r for _ in range(t)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = deque()
queue.append([0, 0])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    if x == t - 1 and y == r - 1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < t and 0 <= ny < r:
            if visited[nx][ny] == 0 and mazeSqure[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))