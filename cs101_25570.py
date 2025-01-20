n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
max_layer = 0
sum_layer = 0
while len(mat) > 1:
    sum_layer = sum(mat[0]) + sum(mat[-1])
    mat.pop(0)
    mat.pop(-1)
    mat_new = []
    for row in mat:
        sum_layer += row[0] + row[-1]
        row.pop(0)
        row.pop(-1)
        mat_new.append(row)
    max_layer = max(max_layer, sum_layer)
    mat = mat_new
if len(mat) == 1:
    max_layer = max(max_layer, mat[0][0])
print(max_layer)