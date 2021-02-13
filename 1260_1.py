def DFS(num):
    print(num, end=' ')  # 처음 방문한 그 지점을 출력
    visited[num] = 1  # 방문했을 때 그 방문리스트에 0으로 되어있을 텐데, 그것을 1로 바꾸어준다.
    for i in range(N+1):
        if visited[i] == 0 and connectList[num][i] == 1:
            DFS(i)

def BFS(num):
    result = [num]
    visited[num] = 0  # 아까 DFS함수를 돌면서 visited리스트의 인덱스값을 모두 1로 바꾸어 주었던 상태이므로 1인상태가 방문을 안한상태이니까 방문을 했을 경우 0으로 바꾸어준다.
    while result:
        num = result[0]
        print(num, end=' ')
        del result[0]
        for i in range(N+1):
            if visited[i] == 1 and connectList[num][i] == 1:
                # print(result)
                result.append(i)
                visited[i] = 0

import sys
N, M, V = map(int, sys.stdin.readline().split())
# N이 정점 개수, M이 간선 개수, V가 시작정점 이라고 생각하고 그래프를 그리는 것이라고 생각하고 코딩 시작.
# 간선 개수>
# 그래프를 컴퓨터가 이해하도록 설계하려면 matrix로 설계를 해야 컴퓨터가 이해를 합니다.
# matrix를 설계와 동시에 초기화까지 시켜줍니다.

connectList = [[0] * (N + 1) for _ in range(N + 1)]
# print(ablist)
# 내가 방문한 점을 또 방문하면 안되니까 visited라는 1차원 행렬을 만들어줍니다.
visited = [0 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connectList[a][b] = 1
    connectList[b][a] = 1

DFS(V)
print()
BFS(V)