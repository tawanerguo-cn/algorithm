T = int(input())
dir = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
def dfs(x,y,board,n,m,visited):
    area = 1
    stack = [(x,y)]
    visited[x][y] = True
    while stack:
        cx,cy = stack.pop()
        for dx,dy in dir:
            nx,ny = dx + cx,dy + cy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 'W':
                visited[nx][ny] = True
                stack.append((nx,ny))
                area += 1
    return area
max_area_list = []
for _ in range(T):
    n,m = map(int,input().split())
    board = [input().strip() for _ in range(n)]
    max_area = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'W' and not visited[i][j]:
                max_area = max(max_area,dfs(i,j,board,n,m,visited))
    max_area_list.append(max_area)
for i in max_area_list:
    print(i)