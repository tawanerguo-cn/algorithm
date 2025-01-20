n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
dp = [[0, 0, 0] for _ in range(n + 1)]
#已知有前i个时最后一个不选，选1，选2的最大身高
#则加上第i + 1个时，不选最大为前面两个选1/2最大
#选1为前面两个选2/不选最大
for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + h1[i - 1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + h2[i - 1]
print(max(dp[-1]))