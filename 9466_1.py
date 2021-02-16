import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방

def DFS(num):
    global res
    # 처음 방문한 그 지점을 출력
    # print("num:", num, end=' ')
    visited[num] = 1  # 방문했을 때 그 방문리스트에 0으로 되어있을 텐데, 그것을 1로 바꾸어준다.
    cycle.append(num)
    n = numbers[num]

    if visited[n]:
        # print("cycle:", cycle)
        if n in cycle:
            res += cycle[cycle.index(n):]
            # print("res:", res)
        return
    else:
        DFS(n)


TestCase = int(input())

for _ in range(TestCase):
    number = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [1] + [0] * (number + 1)
    res = []
    # cnt = 0
    for i in range(1, number + 1):
        # cnt += 1
        # print(cnt, end="번째 :")
        if not visited[i]:
            cycle = []
            DFS(i)

    print(number - len(res))
