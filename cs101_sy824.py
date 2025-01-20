n, m = map(int,input().split())
maze = []
dir = [(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(n):
    row = list(map(int,input().split()))
    maze.append(row)
def min_path(n, m, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    min_path = [(1,1)]
    min_time = [10000]
    def dfs(i, j, time, path):
        nonlocal min_path
        if (i, j) == (n - 1, m - 1):
            if time < min_time[-1]:
                min_time[-1] = time
                min_path = path[:]#!!!!
            return
        for dx, dy in dir:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 0:
                visited[nx][ny] = True
                path.append((nx + 1,ny + 1))
                dfs(nx, ny, time + 1, path)
                visited[nx][ny] = False
                path.pop()
    dfs(0, 0, 0, [(1,1)])
    return min_path
a = min_path(n, m, maze)
for i in a:
    nx, ny = i
    print(nx,ny)