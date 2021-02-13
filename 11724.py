def DFS(num):
    # print(num, end=' ')  # 처음 방문한 그 지점을 출력
    visited[num] = 1  # 방문했을 때 그 방문리스트에 0으로 되어있을 텐데, 그것을 1로 바꾸어준다.
    for i in range(N):
        if visited[i] == 0 and connectList[num][i] == 1:
            DFS(i)


import sys

N, M = map(int, sys.stdin.readline().split())

connectList = [[0] * (N) for _ in range(N)] #matrix
visited = [0 for _ in range(N)]  # check
notVisitede = [0 for _ in range(N)]

# print(notVisitede)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if i == 0:
        V = a
    connectList[a - 1][b - 1] = 1
    connectList[b - 1][a - 1] = 1

DFS(V)
# print("\n")
# print(connectList)
# print(V)
print(notVisitede)
cnt = 0
print(connectList)
for i in range(N):
    for j in range(N):

        # print(j, end="")
        # print("order:", order)
        if connectList[i][j] == 1:
            # print(j)
            notVisitede[j] = 1
            print(notVisitede)
            # print("check")

# print(visited)

print(notVisitede)
for i in notVisitede:
    if i == 0:
        cnt += 1
sys.stdout.write(str(cnt))
