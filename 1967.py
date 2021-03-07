import sys

sys.setrecursionlimit(10**9)


def DFS(start, tree, weight):
    for node, w in tree[start]:
        if weight[node] == 0:  # 처음 가봤으면
            weight[node] = weight[start] + w
            DFS(node, tree, weight)


n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    startNode, arriveNode, w = map(int, sys.stdin.readline().split())
    tree[startNode].append([arriveNode, w])
    tree[arriveNode].append([startNode, w])

weight1 = [0 for _ in range(n + 1)]
DFS(1, tree, weight1)
weight1[1] = 0

print(tree)
print(weight1)
tmpMax = 0
MaxIndex = 0

for i in range(len(weight1)):
    if tmpMax < weight1[i]:
        tmpMax = weight1[i]
        MaxIndex = i


weight2 = [0 for _ in range(n + 1)]

DFS(MaxIndex, tree, weight2)
weight2[MaxIndex] = 0
print(max(weight2))
