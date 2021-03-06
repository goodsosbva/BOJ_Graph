graph = dict()
v = int(input())
for i in range(v):
    graph[i + 1] = {}

for i in range(v):
    inputList = list(map(int, input().split(' ')))
    for j in range(1, len(inputList) - 1, 2):
        graph[inputList[0]][inputList[j]] = inputList[j + 1]


# 첫 dfs
toVisit = [(1, 0)]
visited = [False for i in range(v)]
visited[0] = True
maxLength = 0
maxNode = 1

while toVisit:
    now, length = toVisit.pop()
    maxLength, maxNode = (length, now) if length > maxLength else (maxLength, maxNode)
    for i in graph[now].keys():
        if not visited[i - 1]:
            visited[i - 1] = True
            toVisit.append((i, length + graph[now][i]))


# 2st dfs
toVisit = [(maxNode, 0)]
visited = [False for i in range(v)]
visited[maxNode - 1] = True
maxLength = 0

while toVisit:
    now, length = toVisit.pop()
    maxLength = length if length > maxLength else maxLength

    for i in graph[now].keys():
        if not visited[i - 1]:
            visited[i - 1] = True
            toVisit.append((i, length + graph[now][i]))


print(maxLength)
