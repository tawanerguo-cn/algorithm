from collections import deque
n, m = map(int,input().split())
maze = []
dir = [(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(n):
    row = list(map(int,input().split()))
    maze.append(row)
def min_way(n, m, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    min_way = [10000]
    q = deque([(0, 0, 0)])
    visited[0][0] = True
    is_solved = False
    while q:
        nx, ny, time = q.popleft()
        if (nx, ny) == (n - 1, m - 1):
            is_solved = True
            min_way[-1] = min(min_way[-1], time)
        for dx, dy in dir:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy] and maze[cx][cy] == 0:
                visited[cx][cy] = True
                q.append((cx,cy,time + 1))
    return is_solved, min_way[-1]
is_solved, a = min_way(n, m, maze)
if is_solved:
    print(a)
else:
    print('-1')