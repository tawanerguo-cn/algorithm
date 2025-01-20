m = int(input())
n = int(input())
num = list(map(str, input().split()))
len_num = [len(num[i]) for i in range(n)]
dp = [[[[], 0] for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j < len_num[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            num_i1_j = dp[i - 1][j][1]
            dp_ij_list = dp[i - 1][j - len_num[i - 1]][0]+[num[i - 1]]
            dp_ij_list.sort(key = lambda x:x * 20, reverse = True)
            num_ij_str = ''.join(dp_ij_list)
            num_ij = int(num_ij_str) if num_ij_str else 0
            if num_ij >= num_i1_j:
                dp[i][j][0] = dp_ij_list
                dp[i][j][1] = num_ij
            else:
                dp[i][j] = dp[i - 1][j]

result = dp[-1][-1][1]
print(result if result else '0')
