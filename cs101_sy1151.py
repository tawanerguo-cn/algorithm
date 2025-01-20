s = input()
n = len(s)
dp = [[False for _ in range(n)] for _ in range(n)]
max_len = 1
for i in range(n):
    dp[i][i] = True
for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        if s[i] == s[j]:
            if l == 2:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i + 1][j - 1]
            if dp[i][j]:
                max_len = max(max_len, l)
print(max_len)