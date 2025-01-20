from collections import deque
dir = [(1,0),(-1,0),(0,1),(0,-1)]
m,n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
def bfs(m,n,board,visited):
    length = 0
    visited[0][0] = True
    queue = deque([(0,0,0)])
    while queue:
        x,y,steps = queue.popleft()
        if board[x][y] == 1:
            return steps
        for dx,dy in dir:
            nx,ny = x + dx,y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] != 2:
                visited[nx][ny] = True
                queue.append((nx,ny,steps + 1))
    return 'NO'
print(bfs(m,n,board,visited))