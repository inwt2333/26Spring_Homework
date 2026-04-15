# acmoj: 3077
from collections import deque

def solve(n, m, tasks):
    # n 是同学人数, m 是意愿对数
    # tasks 是存储愿意同住的一对同学的列表
    # 一般图的最大匹配需要使用Edmonds带花树算法 (Blossom Algorithm)
    
    adj = [[] for _ in range(n + 1)]
    for u, v in tasks:
        adj[u].append(v)
        adj[v].append(u)

    match = [0] * (n + 1)
    p = [0] * (n + 1)
    base = [0] * (n + 1)
    q = deque()
    inq = [False] * (n + 1)
    vis = [0] * (n + 1)  # Time stamp for LCA

    def lca(root, u, v, times):
        times += 1
        while True:
            if u != 0:
                u = base[u]
                if vis[u] == times:
                    return u
                vis[u] = times
                if u != root:
                    u = p[match[u]]
                else:
                    u = 0
            u, v = v, u

    def mark_blossom(lca, u, v):
        while base[u] != lca:
            p[u] = v
            v = match[u]
            if not inq[v]:
                inq[v] = True
                q.append(v)
            base[u] = base[v] = lca
            u = p[v]

    def bfs(root):
        nonlocal q, inq, p, base, vis
        p = [0] * (n + 1)
        for i in range(1, n + 1):
            base[i] = i
        inq = [False] * (n + 1)
        q = deque([root])
        inq[root] = True
        times = 0

        while q:
            u = q.popleft()
            for v in adj[u]:
                if base[u] == base[v] or match[u] == v:
                    continue
                if v == root or (match[v] != 0 and p[match[v]] != 0):
                    # Found a blossom
                    cur_lca = lca(root, u, v, times)
                    times += 1
                    mark_blossom(cur_lca, u, v)
                    mark_blossom(cur_lca, v, u)
                elif p[v] == 0:
                    p[v] = u
                    if match[v] == 0:
                        # Found an augmenting path
                        curr = v
                        while curr != 0:
                            prev = p[curr]
                            nxt_match = match[prev]
                            match[curr] = prev
                            match[prev] = curr
                            curr = nxt_match
                        return True
                    else:
                        inq[match[v]] = True
                        q.append(match[v])
        return False

    ans = 0
    for i in range(1, n + 1):
        if match[i] == 0 and bfs(i):
            ans += 1
            
    print(ans)
    print(*match[1:])
    return ans



if __name__ == "__main__":
    n, m = map(int, input().split())
    tasks = []
    for _ in range(m):
        a, b = map(int, input().split())
        tasks.append([a, b])
    solve(n, m, tasks)