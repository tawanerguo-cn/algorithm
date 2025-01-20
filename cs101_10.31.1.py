while True:
    try:
        a, b = map(str, input().split())
        a1 = len(a); b1 = len(b)
        dp = [[0 for _ in range(b1 + 1)] for _ in range(a1 + 1)]
        for i in range(1, a1 + 1):
            for j in range(1, b1 + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp[-1][-1])
    except EOFError:
        break