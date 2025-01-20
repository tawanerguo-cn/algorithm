n,m,k = list(map(int,input().split()))
maze = [list(map(int,input().split())) for _ in range(n)]
dir = [(-1,0),(1,0),(0,1),(0,-1)]
def path_k(n, m, k, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    a = False
    def dfs(x, y, step):
        nonlocal a
        if (x, y) == (n - 1, m - 1):
            if step == k:
                a = True
            return
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                dfs(nx, ny, step + 1)
                visited[nx][ny] = False
    dfs(0, 0, 0)
    return a
if path_k(n, m, k, maze):
    print('Yes')
else:
    print('No')