n,m1,m2 = map(int,input().split())
matrix_1 = [[0 for _ in range(n)] for _ in range(n)]
matrix_2 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m1):
    x,y,k = map(int,input().split())
    matrix_1[x][y] = k
for i in range(m2):
    x,y,k = map(int,input().split())
    matrix_2[x][y] = k
p = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            p[i][j] += matrix_1[i][k] * matrix_2[k][j]
for i in range(n):
    for j in range(n):
        if p[i][j] != 0:
            print(i,j,p[i][j])