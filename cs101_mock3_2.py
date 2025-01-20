values = list(map(int, input().strip().split(',')))
n = len(values)
dp1 = [0] * n
dp2 = [0] * n
dp1[0] = values[0]
dp2[0] = values[0]
for i in range(1, n):
    dp1[i] = max(dp1[i - 1] + values[i], values[i])
    dp2[i] = max(dp2[i - 1] + values[i], dp1[i - 1])
print(max(dp2))