# acmoj: 3069
def solve(n, m, tasks):
    # n 是能量模块种类数，m 是关卡总数
    # tasks 是存储每个关卡两个可选模块的列表
    
    def dfs(u, graph, match_y, visited):
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                # 如果模块 v 未被匹配，或者原先匹配的关卡可以找到其他模块
                if match_y[v] == -1 or dfs(match_y[v], graph, match_y, visited):
                    match_y[v] = u
                    return True
        return False

    # match_y[v] = u 表示能量模块 v 被关卡 u 占用
    match_y = [-1] * n
    
    best_p = 0
    # 逐个添加关卡，尝试寻找增广路
    for i in range(m):
        visited = [False] * n
        if dfs(i, tasks, match_y, visited):
            best_p += 1
        else:
            break  # 只要出现不能匹配的关卡，后面的关卡就玩不了了
            
    print(best_p)
    # 按照题目要求输出每个关卡使用的模块
    result = [0] * best_p
    for mod, task in enumerate(match_y):
        if task != -1 and task < best_p:
            result[task] = mod
    for res in result:
        print(res)

if __name__ == "__main__":
    n, m = map(int, input().split())
    tasks = []
    for _ in range(m):
        a, b = map(int, input().split())
        tasks.append([a, b])
    solve(n, m, tasks)
