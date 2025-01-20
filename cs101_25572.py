from collections import deque
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n = int(input())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)
start = None
for i in range(n):
    start_1 = False
    for j in range(n):
        if maze[i][j] == 5:
            if i + 1 < n and maze[i + 1][j] == 5:
                start = (i, j, 0)
            elif j + 1 < n and maze[i][j + 1] == 5:
                start = (i, j, 2)
            start_1 = True
            break
#由于搜索顺序，必然是0型或者2型,即竖排55或者横排55，竖排55的第一个5在（0，n - 1),(0,n)之间，横排的第一个5在(0, n), (0, n - 1)
    if start_1:
        break
def can_end(n, maze, start):
    visited = [[False for _ in range(n)] for _ in range(n)]
    if start[2] == 0:
        visited[i][j] = True
        q = deque()
        q.append((start[0], start[1]))
        while q:
            nx, ny = q.popleft()
            for dx, dy in dir:
                cx, cy = nx + dx, ny + dy
                if 0 <= cx < n - 1 and 0 <= cy < n and not visited[cx][cy]: 
                    if maze[cx][cy] != 1 and maze[cx + 1][cy] != 1:
                        visited[cx][cy] = True
                        q.append((cx, cy))
                    if maze[cx][cy] != 1 and maze[cx + 1][cy] == 9:
                        return 'yes'
                    if maze[cx][cy] == 9 and maze[cx + 1][cy] != 1:
                        return 'yes'
    if start[2] == 2:
        visited[i][j] = True
        q = deque()
        q.append((start[0], start[1]))
        while q:
            nx, ny = q.popleft()
            for dx, dy in dir:
                cx, cy = nx + dx, ny + dy
                if 0 <= cx < n and 0 <= cy < n - 1 and not visited[cx][cy]:
                    if maze[cx][cy] != 1 and maze[cx][cy + 1] != 1:
                        visited[cx][cy] = True
                        q.append((cx, cy))
                    if maze[cx][cy] != 1 and maze[cx][cy + 1] == 9:
                        return 'yes'
                    if maze[cx][cy] == 9 and maze[cx][cy + 1] != 1:
                        return 'yes'
    return 'no'
a = can_end(n, maze, start)
print(a)