n = int(input())
a = list(map(int,input().split()))
dp = [a[i] for i in range(n)]
for i in range(1,n):
        dp[i] = max(dp[i],dp[i] + dp[i - 1])
print(max(dp))