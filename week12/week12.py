from collections import deque
#
# # d = deque([17, 55, 123])  # 이렇게 넣어도 하나씩 다 들어감
# d = deque((17, 55, 123))  # 이렇게 넣어도 하나씩 다 들어감 처음에 선언할때 시퀸스 타입은 언패킹 대서 들어감
# d.append((1,2))  # 튜플 자체도 들어가긴함
# d.appendleft(100)
# d.append(7)
# d.append(-91)
# print(d.popleft())
# print(d.popleft())
#
# for _ in range(len(d)) :
#     print(d.popleft())
#

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

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]

def dfs(g, i, visited) : # 전위 중위, 후위 순회
    visited[i] = 1
    print(chr(ord('A') + i), end = ' ')
    for j in range(len(g[i])) :
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


def bfs(g, i, visited) :  # sns 네트워크 개념 나랑 연결된 애부터 처리한다
    queue = deque([i])
    visited[i] = 1
    while queue :
        start = queue.popleft()
        print(chr(ord('A') + start), end = ' ')
        for j in range(len(g)):
            if g[start][j] == 1 and not visited[j] :
                visited[j] = 1
                queue.append(j)

bfs(graph, 4, visited_bfs)