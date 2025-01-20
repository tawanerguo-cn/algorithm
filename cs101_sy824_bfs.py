#最短路径问题通常使用bfs,既然可以存储点，也可以存储到达这个点所需的路径
from collections import deque
n, m = map(int,input().split())
maze = []
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(n):
    row = list(map(int,input().split()))
    maze.append(row)
def min_path(n, m, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    min_length = [0]
    min_path = []
    q = deque([(0, 0, 0, [(1, 1)])])
    while q:
        nx, ny, length, path = q.popleft()
        if (nx, ny) == (n - 1, m - 1):
            min_length[-1] = length
            min_path = path[:]
            break
        for dx, dy in dir:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy] and maze[cx][cy] == 0:
                visited[cx][cy] = True
                q.append((cx, cy, length + 1, path + [(cx + 1, cy + 1)]))
    return min_path
min_path = min_path(n, m, maze)
for i in min_path:
    print(i[0], i[1])
