n = int(input())
a = list(map(int, input().split()))
freq = [0 for _ in range(10 ** 5 + 1)]
for i in range(n):
    freq[a[i]] += 1
dp = [0 for _ in range(10 ** 5 + 1)]
for i in range(10 ** 5 + 1):
    dp[i] = max(i * freq[i] + dp[i - 2], dp[i - 1])
print(dp[-1])