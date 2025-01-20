from collections import deque
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)
def min_step(n, m, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    min_step_maze = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True
    min_step_maze[0][0] = 0
    while q:
        nx, ny, step = q.popleft()
        for dx, dy in dir:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy] and maze[cx][cy] == 0:
                visited[cx][cy] = True
                q.append((cx, cy, step + 1))
                min_step_maze[cx][cy] = step + 1
    return min_step_maze
a = min_step(n, m, maze)
for i in a:
    print(' '.join(str(j) for j in i))