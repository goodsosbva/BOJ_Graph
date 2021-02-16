from collections import Counter
from functools import reduce
from collections import deque

n = int(input())

# 지도 입력
squre = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# 오, 왼, 아래, 위
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


#print(squre)

def BFS(x, y, cnt):
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt

    while q:
        x, y = q.popleft()

        for j in range(4):
            mx, my = x + dx[j], y + dy[j]
            if 0 <= mx < n and 0 <= my < n:
                if squre[mx][my] == 1 and visited[mx][my] == 0:
                    q.append((mx, my))
                    visited[mx][my] = cnt

cnt = 0

for q in range(n):
    for w in range(n):
        if squre[q][w] == 1 and visited[q][w] == 0:
            cnt += 1
            BFS(q, w, cnt)

# print(visited)
print(cnt)
# 각 단지마다 집 개수 출력
# 2차원 배열을 1차원으로 쭈욱 펼치기
ans = reduce(lambda x, y: x+y, visited)
# print(ans)
# 단지로 등록?된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# print(ans)
# cnt(단지번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
# print(ans)
print('\n'.join(map(str, ans)))




