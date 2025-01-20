from collections import deque
dir1 = [(0, -1), (0, 1), (1, 0), (-1, 0)]
dir2 = [(0, 2), (0, -2), (2, 0), (-2, 0)]
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = tuple(map(int, input().split()))
    maze.append(row)
maze = tuple(maze)
def min_step(n, m, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True
    while q:
        nx, ny, step = q.popleft()
        if (nx, ny) == (n - 1, m - 1):
            return step
        for dx, dy in dir1:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy] and maze[cx][cy] == 0:
                visited[cx][cy] = True
                q.append((cx, cy, step + 1))
        for dx, dy in dir2:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy] and maze[(cx + nx) // 2][(cy + ny) // 2] == 0 and maze[cx][cy] == 0:
                visited[cx][cy] =True
                q.append((cx, cy, step + 1))
    return -1
a = min_step(n, m, maze)
print(a)