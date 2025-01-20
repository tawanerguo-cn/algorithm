from collections import deque
dir = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
n, m, x, y = map(int, input().split())
def min_step(n, m, x, y):
    min_step_board = [[-1 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((x - 1, y - 1, 0))
    min_step_board[x - 1][y - 1] = 0
    visited[x - 1][y - 1] = True
    while q:
        nx, ny, step = q.popleft()
        for dx, dy in dir:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy]:
                visited[cx][cy] = True
                q.append((cx, cy, step + 1))
                min_step_board[cx][cy] = step + 1
    return min_step_board
a = min_step(n, m, x, y)
for i in a:
    print(' '.join(str(j) for j in i))