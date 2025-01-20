n = int(input())
a = list(map(int,input().split()))
dp = [[a[i],1] for i in range(n)]
for i in range(n-1,0,-1):
    if dp[i][0] > 0:
        dp[i-1][0] = dp[i][0] + dp[i-1][0]
        dp[i-1][1] = dp[i][1] + 1
max_sum = max(dp,key = lambda x:x[0])
max_start = dp.index(max_sum)
max_end = max_start + dp[max_start][1] - 1
print(max_sum[0],max_start + 1,max_end + 1)