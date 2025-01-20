n,a,b,c = map(int,input().split())
dp = [1 if i in [a,b,c] else 0 for i in range(n+1)]
for i in range(1,n+1):
    if dp[max(i-a,0)] != 0 or dp[max(i-b,0)] != 0 or dp[max(i-c,0)] != 0:
        dp[i] = max(dp[max(i-a,0)]+1,dp[max(i-b,0)]+1,dp[max(i-c,0)]+1)
print(dp[n])