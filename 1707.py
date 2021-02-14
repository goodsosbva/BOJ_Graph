import sys
from collections import deque


def BFS(st):
    q = deque()
    q.append(st)  # 아까 DFS함수를 돌면서 visited리스트의 인덱스값을 모두 1로 바꾸어 주었던 상태이므로 1인상태가 방문을 안한상태이니까 방문을 했을 경우 0으로 바꾸어준다.
    visitedList[st] = 1

    while q:
        N = q.popleft()
        print(q, end=' ')
        for index in connected[N]:
            if visitedList[index] == -1:  # 배정 x
                if visitedList[N] == 1:
                    visitedList[index] = 2
                elif visitedList[N] == 2:
                    visitedList[index] = 1
                q.append(index)
            elif visitedList[index] == visitedList[N]:  # 인접한 부분이 같으면 이분 그래프가 아니다.
                return 0
    return 1
        # print(result)


testCase = int(sys.stdin.readline())
for _ in range(testCase):
    N, M = map(int, sys.stdin.readline().split())
    connected = [set() for _ in range(N + 1)]
    #print("connect:", connected)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())

        connected[a].add(b)
        connected[b].add(a)
        print("connect1:", connected)

    visitedList = [-1] * (N + 1)  # matrix
    flag = True

    for q in range(1, N + 1):
        if visitedList[q] == -1:
            tmp = BFS(q)
            if not tmp:
                print(q)
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")
