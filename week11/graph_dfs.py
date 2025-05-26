from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited) : # 전위 중위, 후위 순회
    visited[i] = 1
    print(chr(ord('A') + i), end = ' ')
    for j in range(len(g[i])) :
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


def bfs(g, i, visited) :  # sns 네트워크 개념 나랑 연결된 애부터 처리한다
    queue = deque()
    queue.append(i)
    visited[i] = 1
    while queue :
        start = queue.popleft()
        print(chr(ord('A') + start), end = ' ')
        for j in range(len(g)):
            if g[start][j] == 1 and not visited[j] :
                visited[j] = 1
                queue.append(j)

# 항상 행과 열로 컨트롤 할 생각할 것 -> 인접 행렬
visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
print()
dfs(graph, 6, visited_dfs)
print()
bfs(graph, 5, visited_bfs)