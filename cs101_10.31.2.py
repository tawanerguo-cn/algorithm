n = int(input())
a = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n + 1)]
for i in range(1, n + 1):
    if a[i - 1] == 0:
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = 0
    elif a[i - 1] == 1:
        if dp[i - 1][1] == 0:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = 1
        elif dp[i - 1][1] == 1:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = 0
        elif dp[i - 1][1] == 2:
            dp[i][0] = dp[i - 1][0] 
            dp[i][1] = 1
    elif a[i - 1] == 2:
        if dp[i - 1][1] == 0:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = 2
        elif dp[i - 1][1] == 1:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = 2
        elif dp[i - 1][1] == 2:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = 0
    elif a[i - 1] == 3:
        if dp[i - 1][1] == 0:
            dp[i] = dp[i - 1]
        elif dp[i - 1][1] == 1:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = 2
        elif dp[i - 1][1] == 2:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = 1
print(dp[-1][0])