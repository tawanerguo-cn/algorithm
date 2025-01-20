n, m = map(int,input().split())
weight = [list(map(int,input().split())) for _ in range(n)]
dir = dir = [(-1,0),(1,0),(0,1),(0,-1)]
def max_weight(n,m,weight):
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_weight1 = float('-inf')
    visited[0][0] = True
    best_path = []
    def dfs(x,y,weight_now,path):
        nonlocal max_weight1,best_path
        if (x,y) == (n - 1, m - 1):
            if weight_now > max_weight1:
                max_weight1 = weight_now
                best_path = path[:]
            return
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                path.append((nx + 1, ny + 1))
                dfs(nx,ny,weight_now + weight[nx][ny],path)
                path.pop()
                visited[nx][ny] = False
    dfs(0,0,weight[0][0],[(1,1)])
    return best_path
best_path = max_weight(n,m,weight)
for x,y in best_path:
    print(x,y)
