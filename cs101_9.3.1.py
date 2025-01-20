from math import log2
t = int(input())
list_pre = [2**i for i in range(47)]
for i in range(t):
    n = int(input())
    if n in list_pre:
        print('NO')
    else:
        print('YES')