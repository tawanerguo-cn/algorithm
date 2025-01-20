n, m = map(int,input().split())
weight = [list(map(int,input().split())) for _ in range(n)]
dir = dir = [(-1,0),(1,0),(0,1),(0,-1)]
def max_weight(n,m,weight):
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_weight1 = [-100000000]
    visited[0][0] = True
    def dfs(x,y,weight_now):
        if (x,y) == (n - 1, m - 1):
            max_weight1[0] = max(max_weight1[0],weight_now)
            return
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,weight_now + weight[nx][ny])
                visited[nx][ny] = False
    dfs(0,0,weight[0][0])
    return max_weight1[0]
print(max_weight(n,m,weight))