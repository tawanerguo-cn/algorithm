n, v = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [0 for _ in range(v + 1)]
for i in range(1, v + 1):
    for j in range(n):
        if i >= w[j]:
            dp[i] = max(dp[i], dp[i - w[j]] + c[j])
print(dp[-1])