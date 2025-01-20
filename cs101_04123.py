T = int(input())
dir = [(1,2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(-1,-2)]
def count_paths(n,m,x,y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    total = [0]
    def dfs(cx,cy,visited_count):
        if visited_count == n * m:
            total[0] += 1
            return
        for dx,dy in dir:
            nx,ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, visited_count + 1)
                visited[nx][ny] = False
    visited[x][y] = True
    dfs(x,y,1)
    return total[0]
for _ in range(T):
    n,m,x,y = map(int,input().split())
    print(count_paths(n,m,x,y))