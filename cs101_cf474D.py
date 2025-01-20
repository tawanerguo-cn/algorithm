t, k = map(int,input().split())
dp = [0 for _ in range(10 ** 5 + 1)]
for i in range(k):
    dp[i] = 1
for i in range(k, 10 ** 5 + 1):
    dp[i] = dp[i - 1] % 1000000007 + dp[i - k] % 1000000007
    dp[i] % 1000000007
sum_dp = [0 for _ in range(10 ** 5 + 1)]
sum_dp[0] = 1
for i in range(1, 10 ** 5 + 1):
    sum_dp[i] = sum_dp[i - 1] + dp[i]
for i in range(t):
    a, b = map(int,input().split())
    print((sum_dp[b] - sum_dp[a-1]) % 1000000007)