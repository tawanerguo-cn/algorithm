tensor = []
row = []
col = []
for _ in range(3):
    row_i,col_i = map(int,input().split())
    row.append(row_i)
    col.append(col_i)
    matrix = []
    for i in range(row[_]):
        matrix.append(list(map(int,input().split())))
    tensor.append(matrix)
if col[0] == row[1] and row[0] == row[2] and col[1] == col[2]:
    matrix_product = [[0 for i in range(col[1])] for j in range(row[0])]
    matrix_print = [[0 for i in range(col[1])] for j in range(row[0])]
    for i in range(row[0]):
        for j in range(col[1]):
            for k in range(col[0]):
                matrix_product[i][j] += tensor[0][i][k] * tensor[1][k][j]
    for i in range(row[0]):
        for j in range(col[1]):
            matrix_print[i][j] = matrix_product[i][j] + tensor[2][i][j]
    for i in range(row[0]):
        print(' '.join(str(matrix_print[i][j]) for j in range(col[1])))
else:
    print('Error!')