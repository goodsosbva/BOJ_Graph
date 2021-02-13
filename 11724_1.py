import sys


def DFS(num):
    # print(num, end=' ')  # 처음 방문한 그 지점을 출력
    visited[num] = 1  # 방문했을 때 그 방문리스트에 0으로 되어있을 텐데, 그것을 1로 바꾸어준다.
    for i in range(N):
        if visited[i] == 0 and connectList[num][i] == 1:
            DFS(i)




N, M = map(int, sys.stdin.readline().split())

connectList = [[0] * N for _ in range(N)]  # matrix
visited = [0 for _ in range(N)]  # check
# notVisitede = [0 for _ in range(N + 1)]

# print(notVisitede)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    # if i == 0:
    #    V = a
    connectList[a - 1][b - 1] = 1
    connectList[b - 1][a - 1] = 1


# print("\n")
# print(connectList)
# print(V)

cnt = 0

for i in range(N):
    if visited[i] == 0:
        DFS(i)
        cnt += 1

print(cnt)
