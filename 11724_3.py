import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
matrix = [[0] * N for _ in range(N)]
check = [0] * N
cnt = 0

def dfs(n):
    check[n] = 1
    for i in range(N):
        if check[i] == 0 and matrix[n][i] == 1:
            dfs(i)


for i in range(M):
    u, v = map(int, sys.stdin.readline().split())

    matrix[u-1][v-1] = 1
    matrix[v-1][u-1] = 1


for i in range(N):
    if check[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)