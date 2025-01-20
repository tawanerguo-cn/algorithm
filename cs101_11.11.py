while True:
    try:
        n = int(input())
        n = n + 1
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[1][0] = 1
        for i in range(2, n + 1):
            for j in range(i // 2):
                dp[i][j] = sum(dp[i - j - 1][:(j + 1)])
            for j in range(i // 2, i):
                dp[i][j] = sum(dp[i - j - 1])
        print(sum(dp[-1]))
    except EOFError:
        break