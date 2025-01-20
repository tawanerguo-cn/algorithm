from math import log
t = int(input())
list_2n = [2**i for i in range(0,21)]
for _ in range(t):
    n = int(input())
    m = int(log(n,2))
    sum_origin = int(0.5 * n * (n + 1))
    sum_minor = 2 ** (m + 1) - 1
    print(sum_origin - 2 * sum_minor)