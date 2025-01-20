n, m = map(int, input().split())
if n < m:
    print(2 ** n)
    exit()
dp = [[0 for _ in range(m)] for _ in range(n + 2 - m)]
dp[0] = [2 ** (m - 1 - i) for i in range(m)]
for i in range(1, n + 2 - m):
    dp[i][0] = sum(dp[i - 1])
    for j in range(m - 1):
        dp[i][j + 1] = dp[i - 1][j]
print(dp[-1][0])