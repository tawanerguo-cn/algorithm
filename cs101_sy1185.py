s = input()
t = input()
n1 = len(s)
n2 = len(t)
dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
for i in range(n1 + 1):
    dp[i][0] = i
for j in range(n2 + 1):
    dp[0][j] = j
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
print(dp[-1][-1])