n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = 1
for i in range(2,n + 1):
    dp[i] = dp[i-1] % 10007 + dp[i-2] % 10007
print(dp[-1] % 10007)
