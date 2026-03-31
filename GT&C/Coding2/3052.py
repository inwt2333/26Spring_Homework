# acmoj: 3052
import sys
from collections import deque

sys.setrecursionlimit(30000)

time = 0
stack = deque()
answer = []

def dfsblk(graph, visited, u, parent_edge_id, d, low):
    global time
    time += 1
    d[u] = time
    low[u] = d[u]
    visited[u] = True
    
    for v, edge_id in graph[u]:
        if not visited[v]:
            stack.append((u, v))
            dfsblk(graph, visited, v, edge_id, d, low)
            low[u] = min(low[u], low[v])
            
            # 找到一个点双连通分量
            if low[v] >= d[u]:
                block_edges = []
                while stack:
                    edge = stack.pop()
                    block_edges.append(edge)
                    if edge == (u, v):
                        break
                
                # 提取点并去重排序
                block = set()
                for eu, ev in block_edges:
                    block.add(eu)
                    block.add(ev)
                block_nodes = sorted(list(block))
                if len(block_nodes) >= 1: # 允许单点自环或者两个点的连通块
                    answer.append(block_nodes)
                    
        elif edge_id != parent_edge_id and d[v] < d[u]:
            # 是后向边（指向祖先），且不是刚刚走过来的那条树边
            stack.append((u, v))
            low[u] = min(low[u], d[v])


if __name__ == '__main__':
    input = sys.stdin.readline

    line = input().strip()
    n, m = map(int, line.split()) # n个点，m条边
    visited = [False] * (n + 1)
    d = [0] * (n + 1)

    low = [n + 2] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append((v, i))
        graph[v].append((u, i))

    for i in range(1, n+1):
        if not visited[i]:
            if not graph[i]:
                continue
            dfsblk(graph, visited, i, -1, d, low)
            
    unique_answer = list(set(tuple(block) for block in answer if len(block) > 1 or (len(block)==1 and graph[block[0]])))

    print(len(unique_answer))
    unique_answer.sort()
    for block in unique_answer:
        print(len(block), *block)

    


    
    

