n, m = map(int,input().split())
mat = []
dir = [(1,0), (-1,0), (0,1), (0,-1)]
for _ in range(n):
    row = list(map(int,input().split()))
    mat.append(row)
def count_area(n, m, mat):
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = [0]
    def dfs(i, j):
        stack = [(i, j)]
        while stack:
            nx, ny = stack.pop()
            for dx, dy in dir:
                cx, cy = nx + dx, ny + dy
                if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy] and mat[cx][cy] == 1:
                    visited[cx][cy] = True
                    stack.append((cx, cy))
        count[-1] += 1
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
    return count
a = count_area(n, m, mat)
print(a[-1])