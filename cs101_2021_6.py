n = int(input())
plan = []
for _ in range(n):
    start, end, good = map(str, input().split())
    start_m, start_d = map(int, start.split('.'))
    end_m, end_d = map(int, end.split('.'))
    start = (start_m - 1) * 31 + start_d - 6
    end = (end_m - 1) * 31 + end_d - 6
    plan.append([start, end, int(good)])
#1.7是第1天，2.20是第45天
plan.sort(key = lambda x:(x[1], x[0]))
dp = [[0 for _ in range(45 + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, 45 + 1):
        if j < plan[i - 1][1]:
            dp[i][j] = dp[i - 1][j]
        elif j >= plan[i - 1][1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][plan[i - 1][0] - 1] + plan[i - 1][2])
print(dp[-1][-1])