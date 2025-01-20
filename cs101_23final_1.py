from math import log2
t = int(input())
for _ in range(t):
    n = int(input())
    sum_1 = int(n * (n + 1) * 0.5)
    m = int(log2(n))
    sum_2 = 2 ** (m + 1) - 1
    print(sum_1 - 2 * sum_2)