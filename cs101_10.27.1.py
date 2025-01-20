k = int(input())
m = list(map(int,input().split()))
dp = [1] * k
for i in range(1,k):
    for j in range(i):
        if m[j] >= m[i]:
            dp[i] = max(dp[i],dp[j] + 1)
            print(dp)
print(max(dp))