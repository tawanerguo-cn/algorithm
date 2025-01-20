n, v = map(int, input().split())
w = list(map(int, input().split()))
dp= [[0 for _ in range(v + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, v + 1):
        if j == w[i - 1]:
            dp[i][j]  = 1 + dp[i - 1][j] % 10007
        else:
            dp[i][j] = dp[i - 1][j] % 10007 + dp[i - 1][j - w[i - 1]] % 10007
print(dp[-1][-1] % 10007)