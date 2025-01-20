n = int(input())
a = list(map(int,input().split()))
dp = [1 for i in range(n)]
for i in range(n-1,-1,-1):
    middle = [0]
    for j in range(i + 1, n):
        if a[i] <= a[j]:
            middle.append(dp[j])
    dp[i] += max(middle)
print(max(dp))