n,m = map(int,input().split())
p = list(map(int,input().split()))
dp = [1 if i in p else -1 for i in range(m + 1)]
for i in range(max(p),m + 1):
    p_list = [i-k for k in p]
    dp_list = [dp[i-k] + 1 for k in p if dp[i-k] != -1]
    if len(dp_list) == 0:
        dp[i] = -1
    else:
        dp[i]  = min(dp_list)
print(dp[m])
