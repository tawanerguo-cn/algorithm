from collections import deque
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def min_length(r, c, k, maze, start, end):
    visited = set()
    q = deque()
    q.append((0, start[0], start[1]))
    visited.add((0, start[0], start[1]))
    while q:
        time, x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            next_time = (time + 1) % k
            if 0 <= nx < r and 0 <= ny < c and (next_time, nx, ny) not in visited:
                c1 = maze[nx][ny]
                if c1 == 'E':
                    return time + 1
                elif c1 != '#' or (c1 == '#' and next_time == 0):
                    q.append((time + 1, nx, ny))
                    visited.add((next_time, nx, ny))
    return -1
t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    maze = [list(input().strip()) for _ in range(r)]
    start = None
    end = None
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    a = min_length(r, c, k, maze, start, end)
    print(a if a != -1 else 'Oop!')

