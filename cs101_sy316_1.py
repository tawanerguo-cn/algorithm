n, m = map(int,input().split())
mat = []
dir = [(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(n):
    row = list(map(int,input().split()))
    mat.append(row)
def max_path(n, m, mat):
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_weight  = [-1000000000]
    max_path = []
    visited[0][0] = True
    def dfs(i,j, weight, path):
        nonlocal max_path
        if (i, j) == (n - 1, m - 1):
            if max_weight[0] < weight:
                max_weight[0] = weight
                max_path = path[:]
            return
        for dx, dy in dir:
            cx, cy = i + dx, j + dy
            if 0 <= cx < n and 0 <= cy < m and not visited[cx][cy]:
                visited[cx][cy] = True
                dfs(cx, cy, weight + mat[cx][cy], path + [(cx + 1, cy + 1)])
                visited[cx][cy] = False
    dfs(0, 0, mat[0][0], [(1, 1)])
    return max_path
max_path = max_path(n, m, mat)
for i in max_path:
    print(i[0],i[1])