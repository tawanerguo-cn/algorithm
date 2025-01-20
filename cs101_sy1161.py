n, m = map(int, input().split())
weight = []
for _ in range(m):
    u1, v1, w1 = map(int, input().split())
    weight.append((u1, v1, w1))
weight.sort(key = lambda x:[x[1], x[0]])
dp = [0 for _ in range(n)]
for i in range(m):
    u, v, w = weight[i][0], weight[i][1], weight[i][2]
    dp[v] = max(dp[v], dp[u] + w)
print(max(dp))