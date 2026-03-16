# acmoj: 3034
import sys


def dfs(graph, visited, start):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

if __name__ == '__main__':
    input = sys.stdin.readline

    while True:
        line = input().strip()
        if not line:
            continue
        if line == '0':
            break

        n, m = map(int, line.split()) # n是城镇数量，m是道路数量
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n+1)
        count = 0

        for i in range(1, n+1):
            if not visited[i]:
                count += 1
                dfs(graph, visited, i)

        print(count-1)

        