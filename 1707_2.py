from collections import deque
import sys


def bfs(st):

    q = deque()
    q.append(st)
    visitedList[st] = 1  # 1구역 배정

    while q:
        N = q.popleft()
        for index in connected[N]:
            print("#index, conneted[N]:", index, connected[N])

            if visitedList[index] == -1:  # 아직 배정 x
                if visitedList[N] == 1:
                    visitedList[index] = 2
                elif visitedList[N] == 2:
                    visitedList[index] = 1
                q.append(index)
            elif visitedList[index] == visitedList[N]:

                return 0
        print("index, conneted[N]:", index, connected[N])
    return 1


if __name__ == "__main__":
    testCase = int(sys.stdin.readline())
    for _ in range(testCase):
        N, M = map(int, sys.stdin.readline().split())  # 정점, 간선
        connected = [set() for _ in range(N + 1)]
        for _ in range(M):
            a, b = map(int, sys.stdin.readline().split())
            connected[a].add(b)
            connected[b].add(a)
            print("connect1:", connected)

        visitedList = [-1] * (N + 1)  # Bipartite Graph
        flag = True
        for i in range(1, N + 1):
            if visitedList[i] == -1:
                temp = bfs(i)
                if not temp:
                    flag = False
                    break

        if flag:
            print("YES")
        else:
            print("NO")