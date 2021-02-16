def Daum(N, M):
    n = str(N)
    res = 0
    for i in n:
        res += pow(int(i), M)
    return res


def DFS(N, M, iteration, check):
    if check[N] != 0:
        # print(N)
        return check[N] - 1

    check[N] = iteration
    # print(N)
    daum = Daum(N, M)
    iteration += 1
    return DFS(daum, M, iteration, check)


import sys

N, M = map(int, sys.stdin.readline().split())
check = [0] * 236197  # 9 ** 5 + 9 ** 5 + 9 ** 5 + 9 ** 5
iteration = 1

print(DFS(N, M, iteration, check))


