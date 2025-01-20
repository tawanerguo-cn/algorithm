def next_perm(n, perm):
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i < 0:
        perm = reversed(perm)
        return perm
    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1
    perm[i], perm[j] = perm[j], perm[i]
    perm[i + 1:] = reversed(perm[i + 1:])
    return perm
n = int(input())
k = int(input())
perm = list(map(int, input().split()))
for _ in range(k):
    perm = next_perm(n, perm)
print(' '.join(str(i) for i in perm))