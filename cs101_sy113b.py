n = int(input())
a = list(map(int,input().split()))
dp = [[a[i]] for i in range(n)]
for i in range(n - 1, -1, -1):
    middle = [0 for _ in range(n)]
    for j in range(i + 1, n):
        if dp[i][-1] <= dp[j][0]:
            middle[j] = len(dp[j])
    max_index_m = middle.index(max(middle))
    if max_index_m >= i + 1:
        dp[i].extend(dp[max_index_m])
len_dp = [len(dp[i]) for i in range(n)]
max_len = max(len_dp)
max_index = len_dp.index(max_len)
print(max_len)
print(' '.join(str(i) for i in dp[max_index]))