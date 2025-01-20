#正确的写法：从后往前找到第一个需要改的数，这个数之后的都是降序排列
#然后再寻找降序排列中，比需要改的数最大的最小数，把这两个数交换位置
#再把交换位置之后的序列按从小到大排列
def next_perm(n, perm):
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i < 0:
        perm = sorted(perm)
        return perm
    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1
    perm[i], perm[j] = perm[j], perm[i]
    perm[i + 1:] = sorted(perm[i + 1:])
    return perm
m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    perm = list(map(int, input().split()))
    for _ in range(k):
        perm = next_perm(n, perm)
    print(' '.join(str(i) for i in perm))