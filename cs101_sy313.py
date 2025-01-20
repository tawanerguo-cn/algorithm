n, m = map(int,input().split())
maze = []
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for _ in range(n):
    row = list(map(int,input().split()))
    maze.append(row)
def count_way(n, m, maze):
    count = [0]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    def dfs(cx, cy):
        if (cx, cy) == (n - 1, m - 1):
            count[-1] += 1
            return
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(nx, ny)
                visited[nx][ny] = False
    dfs(0, 0)
    return count[-1]
c = count_way(n, m, maze)
print(c)