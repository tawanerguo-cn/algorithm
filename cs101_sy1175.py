n, v = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[[0, 0] for _ in range(v + 1)] for _ in range(n + 1)]
for i in range(v + 1):
    dp[0][i][1] = 1
for i in range(1, n + 1):
    for j in range(v + 1):
        if j < w[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            if dp[i - 1][j][0] > dp[i - 1][j - w[i - 1]][0] + c[i - 1]:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j][0] < dp[i - 1][j - w[i - 1]][0] + c[i - 1]:
                dp[i][j][0] = dp[i - 1][j - w[i - 1]][0] + c[i - 1]
                dp[i][j][1] = dp[i - 1][j - w[i - 1]][1]
            else:
                dp[i][j][0] = dp[i - 1][j][0]
                dp[i][j][1] = (dp[i - 1][j][1] + dp[i - 1][j - w[i - 1]][1]) % 10007
print(dp[-1][-1][0], dp[-1][-1][1] % 10007)