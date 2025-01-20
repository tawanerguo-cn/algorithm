n = int(input())
dp = [[[0 for _ in range(i)] for _ in range(i)] for i in range(1,n + 1)]
dp[0] = [[1]]
dp[1] = [[1,2],[4,3]]
for i in range (2,n):
    for j in range(i + 1):
        for k in range(i + 1):
            if j == 0:
                dp[i][j][k] = k + 1
            elif j == i:
                dp[i][j][k] = 3 * i + 1 - k
            elif k == 0 and j != 0 and j != i:
                dp[i][j][k] = 4 * i + 1 - j
            elif k == i and j != 0 and j != i:
                dp[i][j][k] = i + 1 + j
            else:
                dp[i][j][k] = dp[i-2][j-1][k-1] + 4 * i
for i in range(n):
    print(' '.join(str(j) for j in dp[n-1][i]))