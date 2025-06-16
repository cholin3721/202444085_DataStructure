INF = 10e6
visited = [0 for _ in range()]
class Graph :
    def __init__(self, size = 0):
        self.size = size
        self.graph = [[INF for _ in range(size)] for _ in range(size)]

def dfs(g, i, visited) :
    # i 시작 노드
    # g 그래프
    # visited = 내가 방문한 노드

    start = i
    visited[i] = 1

    for next in range(g.size) :
        if g.graph[start][next] != INF and visited[next] == 0:
            dfs(g, next, visited)
        else :
            continue
    return

def dfs_ver2(g, i, visited) :
    stack = list()
    visited[i] = 1
    stack.append(i)
    while stack :
        start = stack.pop()
        for next in range(g.size) :
            if g.graph[start][next] != INF and visited[next] == 0 :
                stack.append(next)
                visited[next] = 1
                continue


