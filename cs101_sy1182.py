n, m = map(int, input().split())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
dp = [[-float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
dp[1][1] = mat[0][0]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i, j) != (1, 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + mat[i - 1][j - 1]
print(dp[-1][-1])