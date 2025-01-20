from collections import deque
dir = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
ob_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m, x, y = map(int, input().split())
k = int(input())
obstacle = []
for _ in range(k):
    x1, y1 = map(int, input().split())
    obstacle.append((x1 - 1, y1 - 1))
def min_step(n, m, x, y, obstacle):
    min_step_board = [[-1 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((x - 1, y - 1, 0))
    min_step_board[x - 1][y - 1] = 0
    visited[x - 1][y - 1] = True
    for i in obstacle:
        visited[i[0]][i[1]] = True
    while q:
        nx, ny, step = q.popleft()
        ob_index = []
        for dx1, dy1 in ob_dir:
            cx1, cy1 = nx + dx1, ny + dy1
            if (cx1, cy1) in obstacle:
                index_c = ob_dir.index((dx1, dy1))
                ob_index.extend([2 * index_c, 2 * index_c + 1])
        for i in range(8):
            if i not in ob_index:
                dx, dy = dir[i][0], dir[i][1]
                cx, cy = nx + dx, ny + dy
                if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy]:
                    q.append((cx, cy, step + 1))
                    visited[cx][cy] = True
                    min_step_board[cx][cy] = step + 1
    return min_step_board
a = min_step(n, m, x, y, obstacle)
for i in a:
    print(' '.join(str(j) for j in i))