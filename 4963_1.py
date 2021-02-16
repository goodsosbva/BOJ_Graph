# 오, 왼, 아래, 위, 대각 위(오), 대각 아래(좌), 대각 위(좌), 대각 아래(오)
dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def NumberOfIsles(w, h):
    # print(w, h)
    # 지도 입력
    # squre = [list(map(int, list(input()))) for _ in range(t)]
    rectangle = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    # print(squre)
    def dfs(x, y):
        visited[x][y] = True
        for q in range(8):
            nx, ny = x + dx[q], y + dy[q]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if rectangle[nx][ny] == 1 and visited[nx][ny] is False:
                dfs(nx, ny)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if rectangle[i][j] == 1 and visited[i][j] is False:
                dfs(i, j)
                cnt += 1
    print(cnt)


while True:
    r, t = input().split()

    r = int(r)
    t = int(t)
    if r == 0 and t == 0:
        break
    else:
        # print(r, t)
        NumberOfIsles(r, t)
