rose = input()
n = len(rose)
dp = [[0, 0] for _ in range(n)]
if rose[0] == 'R':
    dp[0] = [0, 1]
else:
    dp[0] = [1, 0]
#理解思路：重要的其实是变成同一个颜色
#每次加入新的一个时都有可能完全改变全弄成红的策略
for i in range(1, n):
    if rose[i] == 'R':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
    else:
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + 1
        dp[i][1] = dp[i - 1][1]
print(dp[-1][0])