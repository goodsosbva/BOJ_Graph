# import sys
# input = sys.stdin.readline
# 오, 왼, 아래, 위, 대각 위(오), 대각 아래(좌), 대각 위(좌), 대각 아래(오)
dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

while True:
    r, t = map(int, input().split())
    if r == 0:
        break
    rectangle = [list(map(int, input().split())) for _ in range(t)]
    visited = [[False] * r for _ in range(t)]


    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= t or ny < 0 or ny >= r:
                continue
            if rectangle[nx][ny] == 1 and visited[nx][ny] is False:
                dfs(nx, ny)

    cnt = 0
    for i in range(t):
        for j in range(r):
            if rectangle[i][j] == 1 and visited[i][j] is False:
                dfs(i, j)
                cnt += 1
    print(cnt)
