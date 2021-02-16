from collections import deque


# 오, 왼, 아래, 위, 대각 위(오), 대각 아래(좌), 대각 위(좌), 대각 아래(오)
dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def NumberOfIsles(r, t):
    # 지도 입력
    # squre = [list(map(int, list(input()))) for _ in range(t)]
    rectangle = [list(map(int, input().split())) for _ in range(t)]
    visited = [[0] * r for _ in range(t)]



    # print(squre)

    def DFS(x, y):
        # q = deque()
        # q.append((x, y))
        visited[x][y] = 1

        # while q:
            # x, y = q.popleft()
            # # print("x, y:", x, y)

        for j in range(8):
            mx, my = x + dx[j], y + dy[j]
                # print("mx, my:", mx, my)
            if 0 <= mx < r and 0 <= my < t:
                if rectangle[mx][my] == 1 and visited[mx][my] == 0:
                    DFS(mx, my)

    cnt = 0

    for q in range(t):
        for w in range(r):
            if rectangle[q][w] == 1 and visited[q][w] == 0:
                cnt += 1
                # print(q, w)
                DFS(q, w)


    # print(visited)
    print(cnt)


while True:
    r, t = input().split()

    r = int(r)
    t = int(t)
    if r == 0 and t == 0:
        break
    else:
        NumberOfIsles(r, t)
