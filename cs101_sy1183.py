n = int(input())
dp = [[0, 0] for _ in range(10 ** 4 + 1)]
dp[1] = [10, 1]
for i in range(2, 10 ** 4 + 1):
    dp[i][0] = ((dp[i - 1][0] - dp[i - 1][1]) * 10 + dp[i - 1][1] * 9) % 10007
    dp[i][1] = (dp[i - 1][0] - dp[i - 1][1]) % 10007
print(dp[n][0] % 10007)