n = int(input())
tower = [list(map(int,input().split())) for _ in range(n)]
dp = [tower[-1][i] for i in range(n)]
for i in range(n-1,0,-1):
    for j in range(i):
        dp[j] = max(dp[j] + tower[i-1][j],dp[j + 1] + tower[i-1][j])
print(dp[0])
