# acmoj: 3036
import sys
bridge = 0

sys.setrecursionlimit(30000)

time = 0

def dfscv(graph, visited, u, d, parent, children, low):
    global time, bridge
    time += 1
    d[u] = time
    low[u] = d[u]
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            children[u] = children[u] + 1
            dfscv(graph, visited, v, d, parent, children, low)
            low[u] = min(low[u], low[v])
            if low[v] > d[u]:
                bridge += 1
        elif v != parent[u]:
            low[u] = min(low[u], d[v])


if __name__ == '__main__':
    input = sys.stdin.readline

    line = input().strip()
    n, m = map(int, line.split()) # n个点，m条边
    visited = [False] * (n + 1)
    d = [0] * (n + 1)
    parent = [0] * (n + 1)
    children = [0] * (n + 1)
    low = [n + 2] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n+1):
        if not visited[i]:
            dfscv(graph, visited, i, d, parent, children, low)

    print(bridge)
    
