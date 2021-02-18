from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 섬의 개수 새기
def findIslandBFS(x, y, cnt):
    q1.append([x, y])
    visited1[x][y] = cnt
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1 and visited1[nx][ny] == 0:
                    visited1[nx][ny] = cnt
                    q1.append([nx, ny])


def bfs2(num):
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1 and visited1[nx][ny] != num:
                    # 섬이 이어지는 다리의 개수 리턴, != num 이아니면 만난 경우로 그 다리수를 리턴해주는것
                    return visited2[x][y] - 1
                if maps[nx][ny] == 0 and visited2[nx][ny] == 0:
                    visited2[nx][ny] = visited2[x][y] + 1
                    q1.append([nx, ny])


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited1 = [[0] * n for _ in range(n)]
q1 = deque()
cnt = 1

# 섬의 개수를 찾는 시작 코드
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited1[i][j] == 0:
            findIslandBFS(i, j, cnt)
            cnt += 1

# print(visited1)
ans = sys.maxsize
# print(ans)
for k in range(1, cnt):
    q1 = deque()
    visited2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1 and visited1[i][j] == k:
                q1.append([i, j])
                visited2[i][j] = 1

    #print("초기", visited2)

    # 섬을 선택해 넓히는 역할을 하는 함수 호출
    res = bfs2(k)
    #print("결과", visited2)
    # print(visited2[0][2])
    ans = min(ans, res)

# print(maps)
print(ans)

