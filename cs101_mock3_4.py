from collections import deque
n = int(input())
map_island = []
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(n):
    row = input()
    map_island.append(row)
def min_length(n, map_island):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    min_length = 10000
    for i in range(n):
        a = False
        for j in range(n):
            if map_island[i][j] == '1':
                stack = [(i, j)]
                q.append((i, j, 0))
                visited[i][j] = True
                a = True
                break
        if a:
            break    
    while stack:
        x, y = stack.pop()
        if not visited[x][y] and map_island[x][y] == '1':
            visited[x][y] = True
            q.append((x, y, 0))
        for dx, dy in dir:
            cx, cy = x + dx, y + dy
            if 0 <= cx < n and 0 <= cy < n and map_island[cx][cy] == '1' and not visited[cx][cy]:
                stack.append((cx, cy))
    while q:
        nx, ny, length = q.popleft()
        for dx, dy in dir:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < n and 0 <= cy < n and not visited[cx][cy]:
                if map_island[cx][cy] == '1':
                    min_length = length
                    return min_length
                else:
                    visited[cx][cy] = True
                    q.append((cx, cy, length + 1))
a = min_length(n, map_island)
print(a)
