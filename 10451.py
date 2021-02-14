def DFS(num):
    #print(num, end=' ')  # 처음 방문한 그 지점을 출력

    visited[num] = 1  # 방문했을 때 그 방문리스트에 0으로 되어있을 텐데, 그것을 1로 바꾸어준다.
    number = numbers[num]
    if not visited[number]:
            #print(number, end="#")
            DFS(number)

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    #print(numbers)
    visited = [1] + [0] * N  # 방문여부확인용
    result = 0

    for i in range(1, N + 1):
        if not visited[i]:
            DFS(i)
            result += 1
    #print("result", result)
    print(result)