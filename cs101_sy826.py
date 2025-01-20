from collections import deque
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = input()
    maze.append(row)
start = None
end = None
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'T':
            end = (i, j)
def min_step(m, n, maze, start):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    while q:
        nx, ny ,step = q.popleft()
        for dx, dy in dir:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy]:
                visited[cx][cy] = True
                if maze[cx][cy] == '.':
                    q.append((cx, cy, step + 1))
                elif maze[cx][cy] == 'T':
                    return step + 1
    return -1
a = min_step(m, n, maze, start)
print(a)