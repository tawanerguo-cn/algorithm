n = int(input())
a = list(map(int,input().split()))
dp = [[1,[a[i]]] for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if a[i] >= a[j]:
            if dp[j][0] + 1 > dp[i][0]:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = dp[j][1] + [a[i]]
dp.sort(key = lambda x: x[0], reverse = True)
print(dp[0][0])
print(' '.join(str(dp[0][1][i]) for i in range(len(dp[0][1]))))