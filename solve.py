def solve(n:int, a:list) -> int:
    visited = [False] * n
    adj = a
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][0] == a[j][0] or a[i][1] == a[j][1]:
                adj[i].append(j)
                adj[j].append(i)

    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs(u)
            
    ans = 0
    for i in range(n):
        if not visited[i]:
            ans += 1
            dfs(i)
    return ans - 1