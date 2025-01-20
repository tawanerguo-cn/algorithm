from collections import deque
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)
trans = []
for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            trans.append((i, j))
trans_1 = trans[0]; trans_2 = trans[1]
def min_step(n, m, maze, trans_1, trans_2):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True
    while q:
        nx, ny, step = q.popleft()
        for dx, dy in dir:
            cx, cy = nx + dx, ny + dy
            if (cx, cy) == (n - 1, m - 1):
                return step + 1
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy]:
                if maze[cx][cy] == 0:
                    q.append((cx, cy, step + 1))
                    visited[cx][cy] = True
                elif (cx, cy) == trans_1:
                    q.append((cx, cy, step + 1))
                    visited[cx][cy] = True
                    q.append((trans_2[0], trans_2[1], step + 1))
                    visited[trans_2[0]][trans_2[1]] = True
                elif (cx, cy) == trans_2:
                    q.append((cx, cy, step + 1))
                    visited[cx][cy] = True
                    q.append((trans_1[0], trans_1[1], step + 1))
                    visited[trans_1[0]][trans_1[1]] = True
    return -1
a = min_step(n, m, maze, trans_1, trans_2)
print(a)