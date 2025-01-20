import math
a = input()
def is_square(num):
    if num == 0:
        return False
    sqrt1 = int(math.sqrt(num))
    return sqrt1 * sqrt1 == num
def is_blessed_number(a):
    n = len(a)
    dp = [False for _ in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            num = int(a[j - 1:i])
            if is_square(num) and dp[j - 1]:
                dp[i] = True
                break
    return dp[n]
if is_blessed_number(a):
    print('Yes')
else:
    print('No')