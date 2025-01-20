n, m1, m2 = map(int, input().split())
mat1 = [[0 for _ in range(n)] for _ in range(n)]
mat2 = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m1):
    i1, j1, value1 = map(int, input().split())
    mat1[i1][j1] = value1
for _ in range(m2):
    i2, j2, value2 = map(int, input().split())
    mat2[i2][j2] = value2
mat3 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            mat3[i][j] += mat1[i][k] * mat2[k][j]
for i in range(n):
    for j in range(n):
        if mat3[i][j] != 0:
            print(i, j, mat3[i][j])