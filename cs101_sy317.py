dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)
weight = []
for _ in range(n):
    row = list(map(int, input().split()))
    weight.append(row)
def max_weight(n, m, maze, weight):
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_weight = [-float('inf')]
    visited[0][0] = True
    def dfs(i, j, weight_now):
        if (i, j) == (n - 1, m - 1):
            max_weight[0] = max(max_weight[0], weight_now)
            return
        for dx, dy in dir:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(nx, ny, weight_now + weight[nx][ny])
                visited[nx][ny] = False
    dfs(0, 0, weight[0][0])
    return max_weight
a = max_weight(n, m, maze, weight)
print(a[0])