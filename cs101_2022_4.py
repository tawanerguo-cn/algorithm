n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
max_sum = 0
for _ in range((n + 1) // 2):
    size = len(mat)
    if size != 1:
        sum_layer = 0
        sum_layer += sum(mat[0])
        sum_layer += sum(mat[-1])
        for i in range(1, size - 1):
            sum_layer += mat[i][0] + mat[i][-1]
            mat[i] = mat[i][1:-1]
        mat = mat[1:-1]
        max_sum = max(sum_layer, max_sum)
    else:
        max_sum = max(mat[0][0], max_sum)
print(max_sum)